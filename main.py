import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Input, concatenate
from tensorflow.keras.callbacks import Callback
import time

base_dir = "CANCER-EYES-ML"
train_dir = "eyes-dataset\Training_Set\Training_Set\Training"
test_dir = "eyes-dataset\Test_Set\Test_Set\Test"
eval_dir = "eyes-dataset\Evaluation_Set\Evaluation_Set\Validation"

csv_training = "eyes-dataset\Training_Set\Training_Set\RFMiD_Training_Labels.csv"
csv_testing = "eyes-dataset\Test_Set\Test_Set\RFMiD_Testing_Labels.csv"
csv_validation = "eyes-dataset\Evaluation_Set\Evaluation_Set\RFMiD_Validation_Labels.csv"

def load_data_from_folder(folder, csv_path):
    dataframe = pd.read_csv(csv_path)
    filename_to_data = dict(zip(dataframe['filename'], dataframe.drop('filename', axis=1).values))
    
    images = []
    csv_data = []
    labels = []
    
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(128, 128))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        images.append(img_array)

        csv_entry = filename_to_data[filename]
        label = csv_entry[0]  # Supposons que la première colonne soit l'étiquette
        csv_data.append(csv_entry[1:])  # Toutes les autres colonnes sont des caractéristiques

        labels.append(label)

    return np.array(images), np.array(csv_data), np.array(labels)

X_train_img, X_train_csv, y_train = load_data_from_folder(train_dir, csv_training)
X_test_img, X_test_csv, y_test = load_data_from_folder(test_dir, csv_testing)
X_eval_img, X_eval_csv, y_eval = load_data_from_folder(eval_dir, csv_validation)

# Normalisation des images
X_train_img = X_train_img / 255.0
X_test_img = X_test_img / 255.0
X_eval_img = X_eval_img / 255.0

# Construction du modèle
img_input = Input(shape=(128, 128, 3))
x = Conv2D(32, (3, 3), activation='relu')(img_input)
x = MaxPooling2D(2, 2)(x)
x = Flatten()(x)
img_features = Dense(128, activation='relu')(x)

csv_input = Input(shape=(X_train_csv.shape[1],))
merged = concatenate([img_features, csv_input])
output = Dense(1, activation='sigmoid')(merged)

model = Model(inputs=[img_input, csv_input], outputs=output)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

class TrainingProgressCallback(Callback):
    def on_epoch_begin(self, epoch, logs=None):
        self.start_time = time.time()

    def on_epoch_end(self, epoch, logs=None):
        elapsed_time = time.time() - self.start_time
        remaining_time = elapsed_time * (self.params['epochs'] - (epoch + 1))
        print(f"Epoch {epoch + 1}/{self.params['epochs']} finished. Elapsed time: {elapsed_time:.2f}s. Remaining time: {remaining_time:.2f}s.")

progress_callback = TrainingProgressCallback()

# Entraînement du modèle avec le callback
model.fit([X_train_img, X_train_csv], y_train, epochs=10, batch_size=32, validation_data=([X_test_img, X_test_csv], y_test), callbacks=[progress_callback])

# Évaluation du modèle sur l'ensemble de test
print("\nPerformance on the test set:")
loss, accuracy = model.evaluate([X_test_img, X_test_csv], y_test)
print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')

# Évaluation du modèle sur l'ensemble d'évaluation
print("\nPerformance on the evaluation set:")
loss_eval, accuracy_eval = model.evaluate([X_eval_img, X_eval_csv], y_eval)
print(f'Loss: {loss_eval}')
print(f'Accuracy: {accuracy_eval}')
