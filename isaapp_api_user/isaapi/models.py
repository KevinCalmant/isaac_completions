"""
models.py
    - Data classes for ISAAP
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    modified_at = db.Column(db.DateTime)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None
     
        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    @classmethod
    def create_user(self, email, password, first_name, last_name): 
        hashed_password = generate_password_hash(password)

        new_user = User(email, hashed_password, first_name, last_name)

        db.session.add(new_user)
        db.session.commit()

        return new_user
 
    def to_dict(self):
        return dict(id=self.id,
                    email=self.email,
                    first_name=self.first_name,
                    last_name=self.last_name,
                    created_at=self.created_at,
                    modified_at=self.modified_at
                    )
