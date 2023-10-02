from flask import Flask, jsonify

app = Flask(__name__, static_folder="../web-eyes/dist", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
