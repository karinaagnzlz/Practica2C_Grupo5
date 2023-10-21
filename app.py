from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)


# Creando la migracion
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, auto_created=True, primary_key=True, serialize=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id,'name': self.name, 'email': self.email}

db.create_all()


# Ruta de ejemplo
@app.route('/status', methods=['GET'])
def test():
  return make_response(jsonify({'response': 'pong'}), 200)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)