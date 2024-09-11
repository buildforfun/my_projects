
from sqlalchemy import create_engine, Column, String, Float, text
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus
import pandas as pd
import numpy as np
import json

Base = declarative_base()

class ElecProdBySource(Base):
    __tablename__ = 'ElecProdBySource'
    Country = Column(String(255), primary_key=True)
    Coal = Column(Float)
    Natural_gas = Column(Float)
    Oil = Column(Float)
    Hydropower = Column(Float)
    Renewable_sources = Column(Float)
    Nuclear = Column(Float)
    Access_to_electricity = Column(Float)

def db_config_json():
    json_file_path = 'db_config.json'
    with open(json_file_path, 'r') as file:
        data_config = json.load(file)
    return data_config

def create_database():

    db_config = db_config_json()
    encoded_password = quote_plus(db_config['password'])

    # database url
    DATABASE_URL = f"mysql+pymysql://{db_config['user']}:{encoded_password}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    # Create the engine for the initial connection (without specifying the database)
    initial_engine = create_engine(f"mysql+pymysql://{db_config['user']}:{encoded_password}@{db_config['host']}:{db_config['port']}")

    # Create the database if it doesn't exist
    with initial_engine.connect() as conn:
        conn.execute(text("CREATE DATABASE IF NOT EXISTS WorldBankData"))

    # Create the engine for the specific database
    engine = create_engine(DATABASE_URL)

    # Creates the table
    Base.metadata.create_all(engine)

    return DATABASE_URL, engine

def insert_data(engine):
    csv_file_path = 'data/processed/3.7_Electricity_production_sources_and_access_processed.csv'
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Replace empty strings with None
    df = df.replace('', None)

    # Replace 'nan' and NaN values with None
    df = df.replace({np.nan: None, 'nan': None})

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Convert DataFrame to list of dictionaries
    data = df.to_dict('records')

    # Bulk insert or update
    for row in data:
        session.merge(ElecProdBySource(**row))

    # Commit the changes
    session.commit()

