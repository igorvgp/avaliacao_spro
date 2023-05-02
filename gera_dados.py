import pandas as pd
from pymongo import MongoClient

# Conectar ao servidor Mongo
client = MongoClient('localhost', 27017)

# Acessar o database onde se encontram as collections
database = client.spro

# Acessar as collections
carros_collection = database.Carros
montadoras_collection = database.Montadoras

# Criar dataframes "Carros" e "Montadoras"
dict_carros = {    'Carro':['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'], 
                     'Cor':['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
               'Montadora':['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']}

dict_montadoras = {'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
                        'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão']}

df_carros = pd.DataFrame(dict_carros)
df_montadoras = pd.DataFrame(dict_montadoras)

# Salvando dataframes em suas respectivas collections
carros_collection.insert_many(df_carros.to_dict(orient='records'))
montadoras_collection.insert_many(df_montadoras.to_dict(orient='records'))
