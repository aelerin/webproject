import repositories.user_repo as userRepo
from models.user_model import User,User_all
import jsonpickle
import json
from flask import session,redirect,url_for,render_template

# défintion d'une méthode pour récupérer les users dans la base de données avec le repo


def get_users():
    data = userRepo.get_users()

    users = jsonpickle.encode(data,max_depth=2)

    return users


def get_user_by_id(user_id):
    data = userRepo.get_user_by_id(user_id)
    user_id = jsonpickle.encode(data,max_depth=2)
    return user_id

def get_user_by_login(user_login):
    data = userRepo.get_user_by_login(user_login)
    user = jsonpickle.encode(data,max_depth=2)
    return user

def create_user(userDto):
    user = User(userDto.nom, userDto.prenom, userDto.naissance, userDto.email, userDto.login, userDto.password)
    return userRepo.create_user(user)


def update_user(user_id,userUpdate):
    
    user = User(userUpdate.nom, userUpdate.prenom, userUpdate.naissance, userUpdate.email, userUpdate.login, userUpdate.password)

    return  userRepo.update_user(user,user_id)


def delete_user(user_id):
    if get_user_by_id(user_id) == 'null':
        return f"Il n'y pas d'utilisateur avec l'id {user_id}"
    else:     
        msg = userRepo.delete_user(user_id)

        return msg


def connect_user(user_request):
    
    user = get_user_by_login(user_request.login)
    if user != "null":
        user=json.loads(user)
        if user_request.login == user["login"] and user_request.password == user["password"]:
            
            return "{\"message\": \"True\", \"url\": \"../profile/profile.html\"}"

    return "{\"message\": \"Erreur lors de la connexion\"}"   
