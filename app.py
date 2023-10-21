from flask import Flask, jsonify

app = Flask(__name__)

# Ruta de ejemplo
@app.route('/')
def hello_world():
    return jsonify(message='Hola, mundo Flask!')

if __name__ == '__main__':
    app.run(debug=True)
