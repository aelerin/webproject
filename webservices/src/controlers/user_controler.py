from flask_classful import FlaskView, route
from flask import jsonify,session,render_template
from flask import abort
from flask import request
import services.user_service as userService
from dto.user_dto import UserDto as userDto
import jsonpickle


# création d'une classe qui hérite de FlaskView


class UsersControler(FlaskView):
    # définition d'une route de base
    route_base = '/api/users/'

    # dééfinition de l'extension de la route de base
    @route('')
    def get_users(self):  # definition d'une méthode pour récupérer les users depuis le service
        users = userService.get_users()  # users récupérer depuis le service
        return users

    @route('<int:user_id>')
    def get_user_by_id(self, user_id):
        user = userService.get_user_by_id(user_id)
        return user

    @route('<user_name>')
    def get_user_by_name(self, user_name):
        user = userService.get_user_by_name(user_name)
        return user

    @route('/', methods=['POST'])
    def create_user(self):
        nom = request.json['nom']
        prenom = request.json['prenom']
        naissance = request.json['naissance']
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']
        user = userDto(nom, prenom, naissance, email, login, password)
        print(user)
        
        return userService.create_user(user)

    @route('<int:user_id>', methods=['PUT'])
    def update_user(self, user_id):
        nom = request.json['nom']
        prenom = request.json['prenom']
        naissance = request.json['naissance']
        email = request.json['email']
        login = request.json['login']
        password = request.json['password']
        userUpdate = userDto(nom, prenom, naissance, email, login, password)
        user = userService.get_user_by_id(user_id)
        user= json.loads(user)
        user = userDto(user['nom'], user['prenom'], naissance['naissance'], email['email'], login['login'], password['password'])
        return jsonify(userService.update_user(user_id,userUpdate, user))

    @route('<int:user_id>', methods=['DELETE'])
    def delete_user(self, user_id):
        result = userService.delete_user(user_id)
        return jsonify(result)


    @route('login', methods=['GET','POST'])
    def login(self):
        if request.method == 'POST' :
            session.pop('user_id', None)

            login = request.json['login']
            password = request.json['password']
            user_request = userDto("","","","",login, password)

        return userService.connect_user(user_request)


    # @route('profile')
    # def profile():
    #     return render_template('profile.html')