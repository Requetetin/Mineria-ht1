import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
from scipy.stats import shapiro
import matplotlib.pyplot as plt
from scipy.stats import shapiro


# base de datos y ver el nombre de cada una de las columnas
movies = pd.read_csv("./movies.csv", encoding="latin1")
movies.columns = [f"pres_{col}" for col in movies.columns]
a = movies.keys()
#print(a, '\n')

#--------------------- Distribución de popularity
print("Distribución de popularity")
popularity = movies['pres_popularity']
print(popularity.describe(include='all'), '\n') 

stat, p = shapiro(popularity)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')


#--------------------- Distribución de budget
print("\nDistribución de budget")
buget = movies['pres_budget']
print(buget.describe(include='all'), '\n') 

stat, p = shapiro(buget)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de revenue
print("\nDistribución de revenue")
revenue = movies['pres_revenue']
print(revenue.describe(include='all'), '\n') 

stat, p = shapiro(revenue)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

# --------------------- Distribución de runtime
print("\nDistribución de runtime")
runtime = movies['pres_runtime']
print(runtime.describe(include='all'), '\n') 

stat, p = shapiro(runtime)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de genresAmount
print("\nDistribución de genresAmount")
genresAmount = movies['pres_genresAmount']
print(genresAmount.describe(include='all'), '\n') 

stat, p = shapiro(genresAmount)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de productionCoAmount
print("\nDistribución de productionCoAmount")
productionCoAmount = movies['pres_productionCoAmount']
print(productionCoAmount.describe(include='all'), '\n') 

stat, p = shapiro(productionCoAmount)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de productionCountriesAmount
print("\nDistribución de productionCountriesAmount")
productionCountriesAmount = movies['pres_productionCountriesAmount']
print(productionCountriesAmount.describe(include='all'), '\n') 

stat, p = shapiro(productionCountriesAmount)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de voteCount
print("\nDistribución de voteCount")
voteCount = movies['pres_voteCount']
print(voteCount.describe(include='all'), '\n') 

stat, p = shapiro(voteCount)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

#--------------------- Distribución de voteAvg
print("\nDistribución de voteAvg")
voteAvg = movies['pres_voteAvg']
print(voteAvg.describe(include='all'), '\n') 

stat, p = shapiro(voteAvg)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')


#--------------------- Distribución de actorsAmount
print("\nDistribución de actorsAmount")
actorsAmount = movies['pres_actorsAmount']
print(actorsAmount.describe(include='all'), '\n') 

stat, p = shapiro(actorsAmount)
print('¿Es distribución normal?\n','Estadisticos=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
   print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
else:
   print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')