from flask import Blueprint, request, jsonify
from .models import User
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json

    user = User(
        username=data['username'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    result = []
    for user in users:
        result.append({
            "id": user.id,
            "username": user.username
        })

    return jsonify(result)

@main.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    data = request.json

    user.username = data['username']
    db.session.commit()

    return jsonify({"message": "Updated"})

@main.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Deleted"})



import jwt
import datetime
from flask import current_app

@main.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(username=data['username']).first()

    if not user or user.password != data['password']:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({"token": token})

from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from flask import request
        
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"message": "Token missing"}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated

@main.route('/protected')
@token_required
def protected():
    return jsonify({"message": "Access granted"})