import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import joblib

import matplotlib.pyplot as plt
from tqdm import tqdm

# Chemins de fichiers
validation_csv_path = "eyes-dataset/Evaluation_Set/Evaluation_Set/RFMiD_Validation_Labels.csv"
validation_dir = "eyes-dataset/Evaluation_Set/Evaluation_Set/Validation"

# Fonction pour pré-traiter les données
def preprocess_data(df, directory):
    images = []
    labels = df["Disease_Risk"].values
    
    for img_name in tqdm(df["ID"], desc="Processing images"):
        img_path = directory + "/" + img_name
        img = load_img(img_path, target_size=(150,150))
        img_array = img_to_array(img) / 255.0
        flat_img_array = img_array.flatten()
        images.append(flat_img_array)
    
    return np.array(images), labels

# Chargement et préparation des données de validation
validation_labels = pd.read_csv(validation_csv_path, dtype={'ID': str, 'Disease_Risk': str})
validation_labels['ID'] = validation_labels['ID'].apply(lambda x: f"{x}.png")
validation_images, validation_labels = preprocess_data(validation_labels, validation_dir)

# Charger et évaluer chaque modèle


# Load and apply PCA transformation
pca = joblib.load('models/PCA.joblib')
validation_images_pca = pca.transform(validation_images)

models = {
    "Random Forest": joblib.load("models/Random Forest.joblib"),
    "SVM": joblib.load("models/SVM.joblib"),
    "K-NN": None,  # K-NN n'est pas sauvegardé précédemment
    "Logistic Regression": joblib.load("models/Logistic Regression.joblib"),
    "PCA + Random Forest": joblib.load("models/PCA + Random Forest.joblib"),
    "eyes_model": load_model("models/eyes_model.h5")
}

scores = {}

for name, model in models.items():
    if model:
        if name == "eyes_model":
            validation_images_reshaped = validation_images.reshape(-1, 150, 150, 3)
            loss, accuracy = model.evaluate(validation_images_reshaped, validation_labels, verbose=0)
        elif "PCA" in name:  # Using PCA transformed data for relevant models
            accuracy = model.score(validation_images_pca, validation_labels)
        else:
            accuracy = model.score(validation_images, validation_labels)
