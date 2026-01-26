import pandas as pd
from sqlalchemy import create_engine

# Tes paramètres de connexion
username = "root"
password = "Mot2passeWild"  # Laisse vide si tu n'as pas de mot de passe, sinon mets-le
host = "localhost"
port = 3306
database = "vanessa_db" # On utilise ta base déjà créée

# Création de la connexion
DATABASE_URI = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)

# Liste des tables à importer depuis le GitHub de dbt
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

print("🚀 Début de l'importation...")

for table in liste_tables:
   csv_url = f"https://github.com/dbt-labs/jaffle-shop-data/raw/refs/heads/main/jaffle-data/raw_{table}.csv"
   df = pd.read_csv(csv_url)
   # On injecte dans MySQL
   df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
   print(f"✅ Table raw_{table} importée !")

print("✨ Terminé ! Tes données t'attendent dans MySQL Workbench.")
