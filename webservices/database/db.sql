USE users
CREATE TABLE users
(
    id INT PRIMARY KEY NOT NULL
    AUTO_INCREMENT,
    nom VARCHAR
    (50) NOT NULL,
    prenom VARCHAR
    (50) NOT NULL,
    naissance VARCHAR
    (10) NOT NULL,
    email VARCHAR
    (50) NOT NULL UNIQUE,
    login VARCHAR
    (20) NOT NULL UNIQUE,
    password VARCHAR
    (30) NOT NULL
    );