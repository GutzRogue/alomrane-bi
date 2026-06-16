from faker import Faker
import pandas as pd
import random
from datetime import date, timedelta

fake = Faker("fr_FR")
random.seed(42)
Faker.seed(42)

REGIONS = {
    "Casablanca-Settat": ["Casablanca", "Mohammedia", "El Jadida"],
    "Rabat-Sale-Kenitra": ["Rabat", "Sale", "Kenitra"],
    "Marrakech-Safi": ["Marrakech", "Safi"],
    "Tanger-Tetouan-Al Hoceima": ["Tanger", "Tetouan"],
    "Fes-Meknes": ["Fes", "Meknes"],
    "Souss-Massa": ["Agadir"]
}

TYPES_BIENS = ["Appartement", "Villa", "Terrain", "Bureau", "Commerce"]

def random_date(start, end):
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

clients = []
for i in range(1, 101):
    clients.append({
        "id_client": i,
        "nom": fake.last_name(),
        "prenom": fake.first_name(),
        "adresse": fake.street_address()[:45],
        "telephone": fake.phone_number()[:45],
        "email": fake.email()[:45]
    })

agents = []
for i in range(1, 21):
    agents.append({
        "id_agent": i,
        "nom": fake.last_name(),
        "prenom": fake.first_name(),
        "email": fake.email()[:45],
        "adresse": fake.street_address()[:45]
    })

projets = []
for i in range(1, 16):
    start = random_date(date(2020, 1, 1), date(2024, 1, 1))
    end = start + timedelta(days=random.randint(365, 1200))
    projets.append({
        "id_projet": i,
        "nom_projet": f"Projet {fake.word().capitalize()}"[:45],
        "date_debut": start.isoformat(),
        "date_fin": end.isoformat()
    })

biens = []
for i in range(1, 201):
    region = random.choice(list(REGIONS.keys()))
    ville = random.choice(REGIONS[region])
    type_bien = random.choice(TYPES_BIENS)
    pieces = random.randint(1, 7)

    base_price = {
        "Appartement": 850000,
        "Villa": 2500000,
        "Terrain": 700000,
        "Bureau": 1200000,
        "Commerce": 1600000
    }[type_bien]

    prix = round(base_price * random.uniform(0.75, 1.45), 2)

    biens.append({
        "id_bien": i,
        "type_bien": type_bien,
        "nombre_piece": str(pieces),
        "prix_affiche": prix,
        "region": region,
        "ville": ville,
        "adresse": fake.street_address()[:45],
        "id_projet": random.randint(1, 15)
    })

transactions = []
used_keys = set()

while len(transactions) < 1000:
    bien = random.choice(biens)
    id_bien = bien["id_bien"]
    id_client = random.randint(1, 100)
    id_agent = random.randint(1, 20)
    tx_date = random_date(date(2021, 1, 1), date(2025, 12, 31)).isoformat()

    key = (id_bien, id_client, id_agent, tx_date)
    if key in used_keys:
        continue

    used_keys.add(key)

    montant = round(float(bien["prix_affiche"]) * random.uniform(0.90, 1.10), 2)

    transactions.append({
        "id_bien": id_bien,
        "id_client": id_client,
        "id_agent": id_agent,
        "date_transaction": tx_date,
        "montant": montant
    })

pd.DataFrame(clients).to_csv("data/clients.csv", index=False)
pd.DataFrame(agents).to_csv("data/agents_immobilier.csv", index=False)
pd.DataFrame(projets).to_csv("data/projets.csv", index=False)
pd.DataFrame(biens).to_csv("data/biens_immobilier.csv", index=False)
pd.DataFrame(transactions).to_csv("data/transactions.csv", index=False)

print("Dataset generated:")
print("clients.csv")
print("agents_immobilier.csv")
print("projets.csv")
print("biens_immobilier.csv")
print("transactions.csv")