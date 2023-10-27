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
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score
import time

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

datagen = ImageDataGenerator(rescale=1./255)
train_data = datagen.flow_from_dataframe(dataframe=train_labels, directory=train_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32)
validation_data = datagen.flow_from_dataframe(dataframe=validation_labels, directory=validation_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32)

train_images, train_labels = preprocess_data(train_labels, train_dir)
validation_images, validation_labels = preprocess_data(validation_labels, validation_dir)
# test_images, test_labels = preprocess_data(test_labels, test_dir)
start_time = time.time()
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

def calculate_metrics(y_true, y_pred, y_prob=None):
    results = {}
    results['accuracy'] = accuracy_score(y_true, y_pred)
    results['recall'] = recall_score(y_true, y_pred, average='weighted')
    results['precision'] = precision_score(y_true, y_pred, average='weighted')
    results['f1'] = f1_score(y_true, y_pred, average='weighted')
    
    if y_prob is not None:
        results['auc_roc'] = roc_auc_score(y_true, y_prob)
    else:
        results['auc_roc'] = 'NA'
        
    return results


test_data = datagen.flow_from_dataframe(dataframe=test_labels, directory=test_dir, x_col="ID", y_col="Disease_Risk", class_mode="binary", target_size=(150,150), batch_size=32, shuffle=False)
all_results = {}
X_test = []
y_test = test_data.classes
for images, _ in test_data:
    X_test.extend(images)
X_test = np.array(X_test)

history = model.fit(train_data, epochs=10, validation_data=validation_data)
end_time = time.time()
training_time = end_time - start_time
y_pred = Sequential.predict_classes(X_test)
y_prob = Sequential.predict(X_test)
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['Sequential'] = results

loss, accuracy = model.evaluate(test_data)
print(f"Test accuracy: {accuracy * 100:.2f}%")

# model.save('models/eyes_model.h5')

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

validation_scores = {}
validation_scores["CNN"] = accuracy


# Random Forest
rf = start_time = time.time()
RandomForestClassifier(n_estimators=100)
rf.fit(train_images, train_labels)
end_time = time.time()
training_time = end_time - start_time
y_pred = RandomForestClassifier.predict(X_test)
y_prob = RandomForestClassifier.predict_proba(X_test)[:, 1]
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['RandomForestClassifier'] = results
validation_accuracy_rf = rf.score(validation_images, validation_labels)
validation_scores["Random Forest"] = validation_accuracy_rf

# SVM
svm = start_time = time.time()
SVC(kernel='rbf')
svm.fit(train_images, train_labels)
end_time = time.time()
training_time = end_time - start_time
y_pred = SVC.predict(X_test)
y_prob = SVC.predict_proba(X_test)[:, 1]
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['SVC'] = results
validation_accuracy_svm = svm.score(validation_images, validation_labels)
validation_scores["SVM"] = validation_accuracy_svm

# K-Nearest Neighbors
knn = start_time = time.time()
KNeighborsClassifier(n_neighbors=5)
knn.fit(train_images, train_labels)
end_time = time.time()
training_time = end_time - start_time
y_pred = KNeighborsClassifier.predict(X_test)
y_prob = KNeighborsClassifier.predict_proba(X_test)[:, 1]
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['KNeighborsClassifier'] = results
validation_accuracy_knn = knn.score(validation_images, validation_labels)
validation_scores["K-NN"] = validation_accuracy_knn

# Logistic Regression
logreg = start_time = time.time()
LogisticRegression(max_iter=10000)
logreg.fit(train_images, train_labels)
end_time = time.time()
training_time = end_time - start_time
y_pred = LogisticRegression.predict(X_test)
y_prob = LogisticRegression.predict_proba(X_test)[:, 1]
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['LogisticRegression'] = results
validation_accuracy_logreg = logreg.score(validation_images, validation_labels)
validation_scores["Logistic Regression"] = validation_accuracy_logreg

# PCA + Random Forest
pca = PCA(n_components=100)
train_images_pca = pca.fit_transform(train_images)
validation_images_pca = pca.transform(validation_images)

rf_pca = start_time = time.time()
RandomForestClassifier(n_estimators=100)
rf_pca.fit(train_images_pca, train_labels)
end_time = time.time()
training_time = end_time - start_time
y_pred = RandomForestClassifier.predict(X_test)
y_prob = RandomForestClassifier.predict_proba(X_test)[:, 1]
prediction_time = time.time() - end_time
results = calculate_metrics(y_test, y_pred, y_prob)
results['training_time'] = training_time
results['prediction_time'] = prediction_time
all_results['RandomForestClassifier'] = results
validation_accuracy_rf_pca = rf_pca.score(validation_images_pca, validation_labels)
validation_scores["PCA + Random Forest"] = validation_accuracy_rf_pca

plt.figure(figsize=(10, 6))
plt.bar(validation_scores.keys(), validation_scores.values(), color=['blue', 'green', 'red', 'cyan', 'purple'])
plt.ylabel('Accuracy')
plt.title('Model Validation Accuracy Comparison')
plt.xticks(rotation=45)
plt.ylim([0, 1])
plt.tight_layout()
plt.show()



import numpy as np

labels = list(all_results.keys())
accuracy = [all_results[model]['accuracy'] for model in labels]
recall = [all_results[model]['recall'] for model in labels]
precision = [all_results[model]['precision'] for model in labels]
f1 = [all_results[model]['f1'] for model in labels]
training_time = [all_results[model]['training_time'] for model in labels]
prediction_time = [all_results[model]['prediction_time'] for model in labels]

x = np.arange(len(labels))
width = 0.15

fig, ax1 = plt.subplots(figsize=(15, 8))

color = 'tab:blue'
ax1.set_xlabel('Models')
ax1.set_ylabel('Scores', color=color)
ax1.bar(x - width*2, accuracy, width, label='Accuracy', color='b')
ax1.bar(x - width, recall, width, label='Recall', color='r')
ax1.bar(x, precision, width, label='Precision', color='g')
ax1.bar(x + width, f1, width, label='F1 Score', color='y')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')
ax1.legend()

ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Time (s)', color=color)
ax2.bar(x + width*2, training_time, width, label='Training Time', color='c')
ax2.bar(x + width*3, prediction_time, width, label='Prediction Time', color='m')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper left', bbox_to_anchor=(0, 0.9))

fig.tight_layout()
plt.title('Model Comparison')
plt.show()
