from flask import Flask, request, jsonify, make_response
from Flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)



##Creando la migracion

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'username': self.username, 'email': self.email}

db.create_all()

# Ruta de ejemplo
@app.route('/hola')
def hello_world():
    return jsonify(message='Hola, mundo Flask!')

# Ruta de status
@app.route('/status', methods=['GET'])
def test():
  return make_response(jsonify({'response': 'pong'}), 200)




# tomar todos los directorios

# get directorio
@app.route('/directories', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    return make_response(jsonify([user.json() for user in users]), 200)
  except e:
    return make_response(jsonify({'message': 'error getting users'}), 500)


# post directorio
@app.route('/directories', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except e:
    return make_response(jsonify({'message': 'error creating user'}), 500)



# get directorio por id
@app.route('/directories/<int:id>', methods=['GET'])
def get_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting user'}), 500)



# update directorio por id
@app.route('/directories/<int:id>', methods=['PUT'])
def update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      user.username = data['username']
      user.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'user updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error updating user'}), 500)



# delete directorio por id
@app.route('/directories/<int:id>', methods=['DELETE'])
def delete_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      db.session.delete(user)
      db.session.commit()
      return make_response(jsonify({'message': 'user deleted'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error deleting user'}), 500)



##patch directorio por id
@app.route('/directories/<int:id>', methods=['PATCH'])
def partial_update_user(id):
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      data = request.get_json()
      if 'username' in data:
        user.username = data['username']
      if 'email' in data:
        user.email = data['email']
      db.session.commit()
      return make_response(jsonify({'message': 'user partially updated'}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except Exception as e:
    return make_response(jsonify({'message': 'error updating user'}), 500)