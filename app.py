from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io

app = Flask(__name__, static_folder="../web-eyes/dist", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')


app = Flask(__name__)

# Chargement du modèle
model_path = 'models/eyes_model.h5'
model = load_model(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file:
        return jsonify({'error': 'no file'}), 400

    # Convertir l'objet FileStorage en BytesIO
    image_stream = io.BytesIO(file.read())
    image = load_img(image_stream, target_size=(150, 150))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # normaliser comme lors de l'entraînement

    # Prédire l'état de l'œil
    prediction = model.predict(image)
    
    # La sortie est une valeur entre 0 et 1 à cause de la fonction sigmoid. 
    # On peut considérer qu'une valeur > 0.5 signifie que l'œil est cancéreux.
    
    # result = 'Cancerous' if prediction[0][0] > 0.5 else 'Healthy'
    result = prediction[0][0]

    return jsonify({'result': result})

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
