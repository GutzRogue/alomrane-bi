DROP TABLE IF EXISTS fact_ventes CASCADE;
DROP TABLE IF EXISTS dim_temps CASCADE;
DROP TABLE IF EXISTS dim_bien CASCADE;
DROP TABLE IF EXISTS dim_projet CASCADE;
DROP TABLE IF EXISTS dim_agent CASCADE;
DROP TABLE IF EXISTS dim_client CASCADE;

CREATE TABLE dim_client (
    sk_client SERIAL PRIMARY KEY,

    id_client INT,

    nom VARCHAR(45),
    prenom VARCHAR(45),
    adresse VARCHAR(45),
    telephone VARCHAR(45),
    email VARCHAR(45)
);

CREATE TABLE dim_agent (
    sk_agent SERIAL PRIMARY KEY,

    id_agent INT,

    nom VARCHAR(45),
    prenom VARCHAR(45),
    email VARCHAR(45),
    adresse VARCHAR(45)
);

CREATE TABLE dim_projet (
    sk_projet SERIAL PRIMARY KEY,

    id_projet INT,

    nom_projet VARCHAR(45),
    date_debut DATE,
    date_fin DATE
);

CREATE TABLE dim_bien (
    sk_bien SERIAL PRIMARY KEY,

    id_bien INT,

    type_bien VARCHAR(45),
    nombre_piece VARCHAR(45),
    prix_affiche FLOAT,
    region VARCHAR(45),
    ville VARCHAR(45),
    adresse VARCHAR(45)
);

CREATE TABLE dim_temps (
    sk_temps SERIAL PRIMARY KEY,

    date_complete DATE,

    jour INT,
    mois INT,
    annee INT,
    trimestre INT
);

CREATE TABLE fact_ventes (

    sk_fact SERIAL PRIMARY KEY,

    sk_client INT REFERENCES dim_client(sk_client),

    sk_agent INT REFERENCES dim_agent(sk_agent),

    sk_projet INT REFERENCES dim_projet(sk_projet),

    sk_bien INT REFERENCES dim_bien(sk_bien),

    sk_temps INT REFERENCES dim_temps(sk_temps),

    montant FLOAT,

    nombre_transaction INT
)
