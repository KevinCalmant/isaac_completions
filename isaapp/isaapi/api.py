"""
api.py
    - Provides API endpoints for consuming & producing
      REST requests response
"""
# External import 
from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app
from functools import wraps

import jwt

# Internal import
from .models import db, User

api = Blueprint('api', __name__)


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        # Get the authentication headers from HTTP headers
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(email=data['sub']).first()

            if not user:
                raise RuntimeError('User not found')
                return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
    return _verify


@api.route('/users', methods=('GET',))
@token_required
def users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@api.route('/register/', methods=('POST',))
def register():
    data = request.get_json()
    user = User.create_user(**data)

    return jsonify(user.to_dict()), 201


@api.route('/login/', methods=('POST',))
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify({
          'message': 'Invaled credentials', 
          'authenticated': False}), 401

    # Will use SECRET_KEY value that we have defined in config.py
    token = jwt.encode({
      'sub': user.email,
      'iat': datetime.utcnow(),
      'exp': datetime.utcnow() + timedelta(minutes=30)},
      current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})

