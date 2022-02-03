import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
import statistics 

movies = pd.read_csv("./movies.csv", encoding="latin1")
movies.columns = [f"pres_{col}" for col in movies.columns]
a =movies.keys()
print(a)
print ( '-----UNO-----------------------------\n')

#---------------------------company country
# print("Tabla de frecuencia de production Company Country")
# print(movies
#     .groupby("pres_productionCompanyCountry")
#     .agg(frecuency=("pres_productionCompanyCountry", "count")))

#--------------------------- production country
# print("Tabla de frecuencia de production Country")
# print(movies
#     .groupby("pres_productionCountry")
#     .agg(frecuency=("pres_productionCountry", "count")))

#--------------------------- release date
# print("Tabla de frecuencia de release date")
# print(movies
#     .groupby("pres_releaseDate")
#     .agg(frecuency=("pres_releaseDate", "count")))

#--------------------------- actors
# print("Tabla de frecuencia de actors")
# print(movies
#     .groupby("pres_actors")
#     .agg(frecuency=("pres_actors", "count")))

#--------------------------- character
# print("Tabla de  actors character")
# print(movies
#     .groupby("pres_actorsCharacter")
#     .agg(frecuency=("pres_actorsCharacter", "count")))

#---------------------------company id
# print("Tabla de  id")
# print(movies
#     .groupby("pres_id")
#     .agg(frecuency=("pres_id", "count")))

# print("Tabla de  actors character")
# print(movies
#     .groupby("pres_actorsCharacter")
#     .agg(frecuency=("pres_actorsCharacter", "count")))

#https://www.odiolaestadistica.com/estadistica-python/tabla-frecuencia/