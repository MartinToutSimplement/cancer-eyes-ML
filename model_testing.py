import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

# Chemins de fichiers
test_csv_path = "eyes-dataset/Test_Set/Test_Set/RFMiD_Testing_Labels.csv"
test_dir = "eyes-dataset/Test_Set/Test_Set/Test"

# Charger les étiquettes de test
test_labels = pd.read_csv(test_csv_path, dtype={'ID': str, 'Disease_Risk': str})
test_labels['ID'] = test_labels['ID'].apply(lambda x: f"{x}.png")

# Initialisation du générateur d'images
datagen = ImageDataGenerator(rescale=1./255)

# Création du générateur de données de test
test_data = datagen.flow_from_dataframe(
    dataframe=test_labels, 
    directory=test_dir, 
    x_col="ID", 
    y_col="Disease_Risk", 
    class_mode="binary", 
    target_size=(150,150), 
    batch_size=32, 
    shuffle=False  # Important pour que les prédictions correspondent aux étiquettes
)

# Chargement du modèle
model_path = 'models/eyes_model.h5'
model = load_model(model_path)

# Évaluation du modèle sur les données de test
loss, accuracy = model.evaluate(test_data)
print(f"Test accuracy: {accuracy * 100:.2f}%")
