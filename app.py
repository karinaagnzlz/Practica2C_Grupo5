from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Ruta de ejemplo utilizando Flask-RESTful
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hola, mundo Flask-RESTful!'}

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
