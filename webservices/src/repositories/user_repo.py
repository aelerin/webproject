from flask_sqlalchemy import SQLAlchemy
from models.user_model import User,User_all,User_connect
import json
from flask import jsonify

db = SQLAlchemy()

# récupération des données dans la base de données


def get_users():
    users = User_all.query.all()
    return users


def get_user_by_id(user_id):
    user = User_all.query.get(user_id)
    return user

def get_user_by_login(user_login):
    return  User_all.query.filter_by(login = user_login).first()

def create_user(user):
    db.session.add(user)
    db.session.commit()
    return "{\"msg\": \"Utilisateur crée\"}"



def update_user(data,user_id):
    user = db.session.query(User).filter(User.id==user_id).first()
    user.nom = data.nom
    user.prenom = data.prenom
    user.naissance = data.naissance
    user.email = data.email
    user.login = data.login
    user.password = data.password

    db.session.commit()
    return f"L'utilisateur {user.login} a été modifier avec succès"


def delete_user(user_id):
    user = db.session.query(User).filter(User.id==user_id).first()
    db.session.delete(user)
    db.session.commit()
    return f'l\'utilisateur {user.login} a été supprimé'

# def get_users_connect():
#     users = User_connect.query.all()
#     return users