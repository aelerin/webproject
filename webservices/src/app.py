from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from controlers.user_controler import UsersControler
from flask_login import LoginManager

# initialisation de l'application Flask
app = Flask(__name__)
# mise en place des CORS
CORS(app)
# définition d'une variable de configuration pour sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.99.100:3306/users'
# initionalisation de la connexion à la base de données
db = SQLAlchemy(app)
# mise en place du controlleur pour les users
UsersControler.register(app)

#login manager
login_manager = LoginManager()
login_manager.init_app(app) # app is a Flask object

app.secret_key = 'some secret key'
# lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)
