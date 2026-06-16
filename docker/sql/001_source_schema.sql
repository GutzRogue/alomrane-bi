DROP TABLE IF EXISTS
    transactions,
    biens_immobilier,
    projets,
    agents_immobilier,
    clients
CASCADE;

CREATE TABLE clients (
    id_client INT PRIMARY KEY,
    nom VARCHAR(45),
    prenom VARCHAR(45),
    adresse VARCHAR(45),
    telephone VARCHAR(45),
    email VARCHAR(45)
);

CREATE TABLE agents_immobilier (
    id_agent INT PRIMARY KEY,
    nom VARCHAR(45),
    prenom VARCHAR(45),
    email VARCHAR(45),
    adresse VARCHAR(45)
);

CREATE TABLE projets (
    id_projet INT PRIMARY KEY,
    nom_projet VARCHAR(45),
    date_debut DATE,
    date_fin DATE
);

CREATE TABLE biens_immobilier (
    id_bien INT PRIMARY KEY,
    type_bien VARCHAR(45),
    nombre_piece VARCHAR(45),
    prix_affiche FLOAT,
    region VARCHAR(45),
    ville VARCHAR(45),
    adresse VARCHAR(45),
    id_projet INT REFERENCES projets(id_projet)
);

CREATE TABLE transactions (
    id_bien INT REFERENCES biens_immobilier(id_bien),
    id_client INT REFERENCES clients(id_client),
    id_agent INT REFERENCES agents_immobilier(id_agent),
    date_transaction DATE,
    montant FLOAT,
    PRIMARY KEY (id_bien, id_client, id_agent, date_transaction)
);