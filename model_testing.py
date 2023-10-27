import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

test_csv_path = "eyes-dataset/Test_Set/Test_Set/RFMiD_Testing_Labels.csv"
test_dir = "eyes-dataset/Test_Set/Test_Set/Test"

test_labels = pd.read_csv(test_csv_path, dtype={'ID': str, 'Disease_Risk': str})
test_labels['ID'] = test_labels['ID'].apply(lambda x: f"{x}.png")

datagen = ImageDataGenerator(rescale=1./255)

test_data = datagen.flow_from_dataframe(
    dataframe=test_labels, 
    directory=test_dir, 
    x_col="ID", 
    y_col="Disease_Risk", 
    class_mode="binary", 
    target_size=(150,150), 
    batch_size=32, 
    shuffle=False 
)

model_path = 'models/eyes_model.h5'
model = load_model(model_path)

loss, accuracy = model.evaluate(test_data)
print(f"Test accuracy: {accuracy * 100:.2f}%")
