from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Define models
userIdColumn = db.Column('user_id', db.Integer(),
                         db.ForeignKey('user.id'))

roleIdColumn = db.Column('role_id', db.Integer(),
                         db.ForeignKey('role.id'))

roles_users = db.Table('roles_users', userIdColumn, roleIdColumn)


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        return dict(name=self.name, description=self.description)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, password, active, roles):
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

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
   
    def to_dict(self):
        return dict(id=self.id, email=self.email)
