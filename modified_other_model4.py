import pandas as pd
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from tqdm import tqdm
from joblib import dump
import matplotlib.pyplot as plt

# Chemins de fichiers
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

train_images, train_labels = preprocess_data(train_labels, train_dir)
validation_images, validation_labels = preprocess_data(validation_labels, validation_dir)
test_images, test_labels = preprocess_data(test_labels, test_dir)

# This dictionary will hold the validation scores for each model
validation_scores = {}

# Random Forest
rf = RandomForestClassifier(n_estimators=100)
rf.fit(train_images, train_labels)
validation_accuracy_rf = rf.score(validation_images, validation_labels)
validation_scores["Random Forest"] = validation_accuracy_rf

# SVM
svm = SVC(kernel='rbf')
svm.fit(train_images, train_labels)
validation_accuracy_svm = svm.score(validation_images, validation_labels)
validation_scores["SVM"] = validation_accuracy_svm

# K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_images, train_labels)
validation_accuracy_knn = knn.score(validation_images, validation_labels)
validation_scores["K-NN"] = validation_accuracy_knn

# Logistic Regression
logreg = LogisticRegression(max_iter=10000)
logreg.fit(train_images, train_labels)
validation_accuracy_logreg = logreg.score(validation_images, validation_labels)
validation_scores["Logistic Regression"] = validation_accuracy_logreg

# PCA + Random Forest
pca = PCA(n_components=100)
train_images_pca = pca.fit_transform(train_images)
validation_images_pca = pca.transform(validation_images)

rf_pca = RandomForestClassifier(n_estimators=100)
rf_pca.fit(train_images_pca, train_labels)
validation_accuracy_rf_pca = rf_pca.score(validation_images_pca, validation_labels)
validation_scores["PCA + Random Forest"] = validation_accuracy_rf_pca

# Plotting the validation scores
plt.figure(figsize=(10, 6))
plt.bar(validation_scores.keys(), validation_scores.values(), color=['blue', 'green', 'red', 'cyan', 'purple'])
plt.ylabel('Accuracy')
plt.title('Model Validation Accuracy Comparison')
plt.xticks(rotation=45)
plt.ylim([0, 1])
plt.tight_layout()
plt.show()
