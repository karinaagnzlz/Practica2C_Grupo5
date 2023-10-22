from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__) # Crear una instancia de la aplicación Flask
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') # Configurar la URI de la base de datos desde la variable de entorno 'DB_URL'
db = SQLAlchemy(app) # Crear una instancia de SQLAlchemy y asociarla a la aplicación

# Crear la tabla en la base de datos utilizando el modelo Directory
class Directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    emails = db.Column(db.ARRAY(db.String), nullable=False)

    def serialize(self):
         return {
            'id': self.id,
            'name': self.name,
            'emails': list(self.emails)
        }

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Endpoint de estado
@app.route('/status/', methods=['GET'])
def get_status():
    return make_response(jsonify({'message:':'pong'}),200)

# Endpoint para listar todos los directorios
@app.route('/directories', methods=['GET'])
def get_directories():
    directories = Directory.query.all()
    serialized_directories = [directory.serialize() for directory in directories]
    response = jsonify(serialized_directories)
    return make_response(response, 200)

# Endpoint para crear un directorio
@app.route('/directories', methods=['POST'])
def create_directory():
    data = request.get_json()
    name = data.get('name')
    emails = data.get('emails')
       
    # Intenta crear un nuevo directorio
    directory = Directory(name=name, emails=emails)
    try:
        db.session.add(directory)
        db.session.commit()
        response = jsonify(directory.serialize())
        return make_response(response, 201)
    except:
        db.session.rollback()
        response = jsonify({'message': 'Error: Ya existe un directorio con esos datos'})
        return make_response(response, 400) 


# Endpoint para obtener, actualizar y eliminar un directorio por su ID
@app.route('/directories/<int:directory_id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
def manage_directory(directory_id):
     directory = Directory.query.get(directory_id)
    
     if directory is None:  # Si el directorio no existe, devolver un mensaje de error y el código de estado 404
         return jsonify({'message': 'Directory not found'}), 404
    
     if request.method == 'GET': # Si la solicitud es GET, devolver la representación serializada del directorio y el código de estado 200
        response = jsonify(directory.serialize())
        return make_response(response, 200)
    
     if request.method == 'PUT': # Si la solicitud es PUT, actualizar el directorio con los datos proporcionados y devolver la representación actualizada
        data = request.get_json()
        directory.name = data.get('name')
        directory.emails = data.get('emails')
        db.session.commit()
        response = jsonify(directory.serialize())
        return make_response(response, 200)
    
     if request.method == 'PATCH':  # Si la solicitud es PATCH, actualizar selectivamente los campos del directorio y devolver la representación actualizada
        data = request.get_json()
        if 'name' in data:
            directory.name = data['name']
        if 'emails' in data:
            directory.emails = data['emails']
        db.session.commit()
        response = jsonify(directory.serialize())
        return make_response(response, 200)
    
     if request.method == 'DELETE': # Si la solicitud es DELETE, eliminar el directorio y devolver un mensaje de éxito
        db.session.delete(directory)
        db.session.commit()
        response = jsonify({'message': 'Directory deleted'})
        return make_response(response, 200)
