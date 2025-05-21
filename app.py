# from flask import Flask, request, jsonify
# from models import db, User
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load DATABASE_URL from .env

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)
# @app.route('/')
# def hello():
#     return "it works!"

# @app.route('/testpost', methods=['POST'])
# def test_post():
#     return jsonify({"message": "POST request received"}), 200

# @app.route('/user', methods=['POST'])
# @app.route('/user/', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(name=data['name'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'User created successfully'}), 201


# @app.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     output = [{'id': user.id, 'name': user.name} for user in users]
#     return jsonify(output), 200

# @app.route('/user/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted successfully'}), 200

# @app.route('/user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404

#     data = request.get_json()
#     user.name = data.get('name', user.name)
#     db.session.commit()
#     return jsonify({'message': 'User updated successfully'}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import logging
import os
from dotenv import load_dotenv
from models import db, User

load_dotenv()  # Load DATABASE_URL from .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello():
    return "it works!"

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    app.logger.info('Creating user with data: %s', data)  # Log user creation
    new_user = User(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    app.logger.info('User  created successfully: %s', new_user.id)  # Log success
    return jsonify({'message': 'User  created successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = [{'id': user.id, 'name': user.name} for user in users]
    app.logger.info('Retrieved users: %s', output)  # Log user retrieval
    return jsonify(output), 200

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        app.logger.warning('User  not found: %s', user_id)  # Log warning
        return jsonify({'error': 'User  not found'}), 404

    db.session.delete(user)
    db.session.commit()
    app.logger.info('User  deleted successfully: %s', user_id)  # Log success
    return jsonify({'message': 'User  deleted successfully'}), 200

@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        app.logger.warning('User  not found: %s', user_id)  # Log warning
        return jsonify({'error': 'User  not found'}), 404

    data = request.get_json()
    user.name = data.get('name', user.name)
    db.session.commit()
    app.logger.info('User  updated successfully: %s', user_id)  # Log success
    return jsonify({'message': 'User  updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
