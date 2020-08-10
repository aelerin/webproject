from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# création d'une classe qui permettra de faire des objets qui mettront en forme les informations recus depuis la BDD


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    naissance = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, nom, prenom, naissance, email, login, password):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.email = email
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<User id:{self.id} nom:{self.nom} prenom:{self.prenom} naissance: {self.naissance} email: {self.email} login: {self.login} password: {self.password}>'

# table_args = {'extend_existing': True}

class User_all(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    login = db.Column(db.String, unique=True)

    def __init__(self, nom, prenom, email, login):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.login = login

    def __repr__(self):
        return f'<User id:{self.id} nom:{self.nom} prenom:{self.prenom} email: {self.email} login: {self.login}>'


class User_connect(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, login, password):

        self.login = login
        self.password = password

    def __repr__(self):
        return f'<User id:{self.id} login: {self.login} password: {self.password}>'