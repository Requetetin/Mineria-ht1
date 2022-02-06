from numpy import *
import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv("./movies.csv", encoding="latin1")

# print(
#   "\nLos datos tienen", len(movies), "observaciones y", len(movies.columns), "variables."
# )

# print(movies.describe())
# print("\n\n\n")
# print(movies.head())

#------------------ Preguntas ------------------
#4.1 mas presupuesto
# budget = movies.nlargest(10, 'budget')['title']
# print("Las 10 peliculas con mas presupuestos fueron \n", budget)
# #4.2
# revenues = movies.nlargest(10, 'revenue')['title']
# print("Las 10 peliculas con mas ingresos fueron \n", revenues)
# #4.3
# mostVoted = movies.nlargest(1, 'voteCount')['title']
# print("La pelicula con mas votos fue: \n", mostVoted)
# #4.4
# worst = movies.nsmallest(1, 'voteAvg')['title']
# print("La peor pelicula segun los votos de los usuarios es:  \n", worst)
# #4.5
# movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
# yearly = movies['releaseDate'].dt.year.value_counts()
# yearly.plot.bar()
# #4.6
# genres = movies['genres'].str.split('|', n=-1)
# genres

#4.7
# movies['mainGenre'] = movies['genres'].str.split('|').str[0]
# print(movies.nlargest(10, 'revenue')['mainGenre'])
# print('\n\n', movies['mainGenre'].value_counts())

# #4.8
# movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
# movies['yearOfRelease'] = movies['releaseDate'].dt.year

# castActors = list(movies['actorsAmount'])
# revenueList = list(movies['revenue'])
# yearList = list(movies['yearOfRelease'])

# realCast, realRevenue, realYear = [], [], []

# for i in range(len(castActors)):
#   try:
#     totalCast = int(castActors[i])
#     revenue = revenueList[i]
#     year = yearList[i]
#     if totalCast < 100:
#       realCast.append(totalCast)
#       realRevenue.append(revenue)
#       realYear.append(year)
#   except:
#     continue

# plt.scatter(realRevenue, realCast)
# plt.ylabel('Actores en el reparto')
# plt.xlabel('Ganancias')
# plt.show()
# print(corrcoef(realRevenue,realCast))

# plt.scatter(realCast, realYear)
# plt.xlabel('Actores en el reparto')
# plt.ylabel('Year')
# plt.show()



# #4.9
# castWomen = list(movies['castWomenAmount'])
# castMen = list(movies['castMenAmount'])
# revenueList = list(movies['revenue'])
# ratings = list(movies['popularity'])

# realW, realM, respectiveRev, respectiveRat = [], [], [], []

# for i in range(len(castWomen)):
#   try:
#     cwomen = int(castWomen[i])
#     cmen = int(castMen[i])
#     revenue = revenueList[i]
#     popularity = ratings[i]
#     if cwomen < 100 and cmen < 100:
#       realW.append(cwomen)
#       realM.append(cmen)
#       respectiveRev.append(revenue)
#       respectiveRat.append(popularity)
#   except:
#     continue

# plt.scatter(respectiveRev,realW)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Ganancias')
# plt.show()
# print(corrcoef(respectiveRev,realW))

# plt.scatter(respectiveRev, realM)
# plt.ylabel('Hombres en el reparto')
# plt.xlabel('Ganancias')
# plt.show()
# print(corrcoef(respectiveRev,realM))

# plt.scatter(respectiveRat, realW)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Ratings')
# plt.show()
# print(corrcoef(respectiveRat,realW))

# plt.scatter(respectiveRat, realM)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Rating')
# plt.show()
# print(corrcoef(respectiveRat,realM))

# #4.11
# plt.scatter(movies.budget, movies.revenue)
# plt.ylabel('Ganancias')
# plt.xlabel('Presupuesto')


# plt.hist(movies.revenue)
# plt.ylabel('Ganancias')

# plt.hist(movies.budget)
# plt.ylabel('Presupuesto')
# plt.show()
#print("Correlacion entre presupuesto y ganancias", movies.revenue.corr(movies.budget))

#4.14
# popularity = movies["popularity"]
# revenue = movies["revenue"]
# voteAvg = movies["voteAvg"]
# correlation = voteAvg.corr(popularity)
# correlation2 = voteAvg.corr(revenue)
# print("\n\nCorrelacion calificaciones con popularidad", correlation, "\nCorrelacion calificaciones con ganancias", correlation2, "\n\n")

# #4.15
# print(movies.nlargest(10, 'runtime')['genres'])
