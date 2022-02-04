import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
import statistics 

# base de datos y ver el nombre de cada una de las columnas
movies = pd.read_csv("./movies.csv", encoding="latin1")
movies.columns = [f"pres_{col}" for col in movies.columns]
a = movies.keys()
print(a, '\n')

#--------------------------- genres
genres = movies['pres_genres'].str.split("|").str[0]
print("Tabla de frecuencia de genres")
print(movies.groupby(genres).agg(frecuency=("pres_genres", "count")))

#--------------------------- Video
print("Tabla de frecuencia de Video")
print(movies
    .groupby("pres_video")
    .agg(frecuency=("pres_video", "count")))

#--------------------------- Original title
print("Tabla de frecuencia de Original titles")
print(movies
    .groupby("pres_originalTitle")
    .agg(frecuency=("pres_originalTitle", "count")))

#--------------------------- Original langauge
print("Tabla de frecuencia de Original Language")
print(movies
    .groupby("pres_originalLanguage")
    .agg(frecuency=("pres_originalLanguage", "count")))

#--------------------------- home page
print("Tabla de frecuencia de HomePage")
print(movies
    .groupby("pres_homePage")
    .agg(frecuency=("pres_homePage", "count")))

#--------------------------- director
print("Tabla de frecuencia de Director")
print(movies
    .groupby("pres_director")
    .agg(frecuency=("pres_director", "count")))

#---------------------------company country
ccompany = movies['pres_productionCompanyCountry'].str.split("|").str[0]
print("Tabla de frecuencia de production company country")
print(movies.groupby(ccompany).agg(frecuency=("pres_productionCompanyCountry", "count")))

#--------------------------- production country)
pcountry = movies['pres_productionCountry'].str.split("|").str[0]
print("Tabla de frecuencia de production country")
print(movies.groupby(pcountry).agg(frecuency=("pres_productionCountry", "count")))

#--------------------------- production Company)
pcompany = movies['pres_productionCompany'].str.split("|").str[0]
print("Tabla de frecuencia de production country")
print(movies.groupby(pcompany).agg(frecuency=("pres_productionCompany", "count")))


#--------------------------- release date
print("Tabla de frecuencia de release date")
print(movies
    .groupby("pres_releaseDate")
    .agg(frecuency=("pres_releaseDate", "count")))

#--------------------------- actors
actors = movies['pres_actors'].str.split("|").str[0]
print("Tabla de frecuencia de actors")
print(movies.groupby(actors).agg(frecuency=("pres_actors", "count")))


#--------------------------- character
character = movies['pres_actorsCharacter'].str.split("|").str[0]
print("Tabla de frecuencia de character")
print(movies.groupby(character).agg(frecuency=("pres_actorsCharacter", "count")))

#---------------------------company id
print("Tabla de  id")
print(movies
    .groupby("pres_id")
    .agg(frecuency=("pres_id", "count")))
