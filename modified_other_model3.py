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

# # Random Forest
# rf = RandomForestClassifier(n_estimators=100)
# rf.fit(train_images, train_labels)
# accuracy = rf.score(test_images, test_labels)
# print(f"Random Forest accuracy: {accuracy * 100:.2f}%")
# dump(rf, "models/Random Forest.joblib")

# # SVM
# svm = SVC(kernel='rbf')
# svm.fit(train_images, train_labels)
# accuracy = svm.score(test_images, test_labels)
# print(f"SVM accuracy: {accuracy * 100:.2f}%")
# dump(svm, "models/SVM.joblib")

# K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_images, train_labels)
accuracy = knn.score(test_images, test_labels)
print(f"K-NN accuracy: {accuracy * 100:.2f}%")
dump(knn, 'models/K-NN.joblib')

# Régression logistique
# logreg = LogisticRegression(max_iter=10000)
# logreg.fit(train_images, train_labels)
# accuracy = logreg.score(test_images, test_labels)
# print(f"Logistic Regression accuracy: {accuracy * 100:.2f}%")
# dump(logreg, "models/Logistic Regression.joblib")

# # PCA + Random Forest
# pca = PCA(n_components=100)  # Réduisez à 100 composants principaux
# train_images_pca = pca.fit_transform(train_images)
# test_images_pca = pca.transform(test_images)

# rf_pca = RandomForestClassifier(n_estimators=100)
# rf_pca.fit(train_images_pca, train_labels)
# accuracy = rf_pca.score(test_images_pca, test_labels)
# print(f"PCA + Random Forest accuracy: {accuracy * 100:.2f}%")
# dump(rf_pca, "models/PCA + Random Forest.joblib")
