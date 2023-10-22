from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@my_postgres_db/practica2b_grupo5'
db = SQLAlchemy(app)


# # Creando la tabla en la base de datos
# class Directory(db.Model):
#         id = db.Column(db.Integer, primary_key=True)
#         name = db.Column(db.String(500), nullable=False, unique=True)
#         emails = db.Column(db.ARRAY(db.String), nullable=False, unique=True)

#         def json(self):
#             return {'id':self.id, 'name':self.name, 'emails':list(self.emails)}
        
# db.create_all()


# Endpoint de estado
@app.route('/status', methods=['GET'])
def get_status():
    return make_response(jsonify({'message:':'pong'}),200)

# # Endpoint para listar todos los directorios
# @app.route('/directories/', methods=['GET'])
# def get_directories():
#     with app.app_context():
#         directories = Directory.query.all()
#     return jsonify([directory.serialize() for directory in directories])

# # Endpoint para crear un directorio
# @app.route('/directories/', methods=['POST'])
# def create_directory():
#     data = request.get_json()
#     name = data.get('name')
#     emails = data.get('emails')
#     directory = Directory(name=name, emails=emails)
#     db.session.add(directory)
#     db.session.commit()
#     return jsonify(directory.serialize()), 201

# # Endpoint para obtener, actualizar y eliminar un directorio por su ID
# @app.route('/directories/<int:directory_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
# def manage_directory(directory_id):
#     directory = Directory.query.get(directory_id)
    
#     if directory is None:
#         return jsonify({'message': 'Directory not found'}), 404
    
#     if request.method == 'GET':
#         return jsonify(directory.serialize())
    
#     if request.method == 'PUT':
#         data = request.get_json()
#         directory.name = data.get('name')
#         directory.emails = data.get('emails')
#         db.session.commit()
#         return jsonify(directory.serialize())
    
#     if request.method == 'PATCH':
#         data = request.get_json()
#         if 'name' in data:
#             directory.name = data['name']
#         if 'emails' in data:
#             directory.emails = data['emails']
#         db.session.commit()
#         return jsonify(directory.serialize())
    
#     if request.method == 'DELETE':
#         db.session.delete(directory)
#         db.session.commit()
#         return jsonify({'message': 'Directory deleted'})
