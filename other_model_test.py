import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from tensorflow.keras.callbacks import EarlyStopping


train_csv_path = "eyes-dataset/Training_Set/Training_Set/RFMiD_Training_Labels.csv"
validation_csv_path = "eyes-dataset/Evaluation_Set/Evaluation_Set/RFMiD_Validation_Labels.csv"
test_csv_path = "eyes-dataset/Test_Set/Test_Set/RFMiD_Testing_Labels.csv"
train_dir = "eyes-dataset/Training_Set/Training_Set/Training"
validation_dir = "eyes-dataset/Evaluation_Set/Evaluation_Set/Validation"
test_dir = "eyes-dataset/Test_Set/Test_Set/Test"

train_labels = pd.read_csv(train_csv_path, dtype={'ID': str, 'Disease_Risk': str})
validation_labels = pd.read_csv(validation_csv_path, dtype={'ID': str, 'Disease_Risk': str})
test_labels = pd.read_csv(test_csv_path, dtype={'ID': str, 'Disease_Risk': str})

train_labels['ID'] = train_labels['ID'].apply(lambda x: f"{x}.png")
validation_labels['ID'] = validation_labels['ID'].apply(lambda x: f"{x}.png")
test_labels['ID'] = test_labels['ID'].apply(lambda x: f"{x}.png")

datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_dataframe(dataframe=train_labels, directory=train_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32)
validation_data = datagen.flow_from_dataframe(dataframe=validation_labels, directory=validation_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32)
test_data = datagen.flow_from_dataframe(dataframe=test_labels, directory=test_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32, shuffle=False)


base_model = VGG16(weights='imagenet', include_top=False, pooling='avg')

def extract_features(generator, sample_count):
    features = np.zeros(shape=(sample_count, 512))
    labels = np.zeros(shape=(sample_count))
    i = 0
    for inputs_batch, labels_batch in generator:
        features_batch = base_model.predict(preprocess_input(inputs_batch))
        features[i * generator.batch_size : (i + 1) * generator.batch_size] = features_batch
        labels[i * generator.batch_size : (i + 1) * generator.batch_size] = labels_batch
        i += 1
        if i * generator.batch_size >= sample_count:
            break
    return features, labels

train_features, train_labels = extract_features(train_data, train_labels.shape[0])
validation_features, validation_labels = extract_features(validation_data, validation_labels.shape[0])

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(train_features, train_labels)

validation_predictions = rf_model.predict(validation_features)
val_acc = accuracy_score(validation_labels, validation_predictions)
print(f"Validation accuracy with Random Forest: {val_acc * 100:.2f}%")

# VGG16 pour la classification
base_model_classification = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))
for layer in base_model_classification.layers:
    layer.trainable = False

x = Flatten()(base_model_classification.output)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(1, activation='sigmoid')(x)

vgg_model = Model(inputs=base_model_classification.input, outputs=predictions)

vgg_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = vgg_model.fit(train_data, epochs=10, validation_data=validation_data)

vgg_model.save('models/vgg16_model.h5')

loss, accuracy = vgg_model.evaluate(test_data)
print(f"Test accuracy with VGG16: {accuracy * 100:.2f}%")