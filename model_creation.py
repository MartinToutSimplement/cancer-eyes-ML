import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator

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


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(train_data, epochs=10, validation_data=validation_data)

test_data = datagen.flow_from_dataframe(dataframe=test_labels, directory=test_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32, shuffle=False)

loss, accuracy = model.evaluate(test_data)
print(f"Test accuracy: {accuracy * 100:.2f}%")

model.save('models/eyes_model.h5')