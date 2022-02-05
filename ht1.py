from numpy import NaN
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
budget = movies.nlargest(10, 'budget')['title']
print("Las 10 peliculas con mas presupuestos fueron \n", budget)
#4.2
revenues = movies.nlargest(10, 'revenue')['title']
print("Las 10 peliculas con mas ingresos fueron \n", revenues)
#4.3
mostVoted = movies.nlargest(1, 'voteCount')['title']
print("La pelicula con mas votos fue: \n", mostVoted)
#4.4
worst = movies.nsmallest(1, 'voteAvg')['title']
print("La peor pelicula segun los votos de los usuarios es:  \n", worst)
#4.5
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
yearly = movies['releaseDate'].dt.year.value_counts()
yearly.plot.bar()
#4.6
genres = movies['genres'].str.split('|', n=-1)
genres

#4.9
movies.castWomenAmount.replace('.*', regex=True, value=NaN)
movies.sort_values("castWomenAmount", inplace = True)
print(movies.castWomenAmount)
# movies.castWomenAmount.where(movies.castWomenAmount > 100 , NaN)

# plt.scatter(movies.revenue, movies.castWomenAmount)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Ganancias')
# plt.show()

# plt.scatter(movies.revenue, movies.castMenAmount)
# plt.ylabel('Hombres en el reparto')
# plt.xlabel('Ganancias')
# plt.show()

# plt.scatter(movies.voteAvg, movies.castWomenAmount)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Ratings')
# plt.show()

# plt.scatter(movies.voteAvg, movies.castMenAmount)
# plt.ylabel('Mujeres en el reparto')
# plt.xlabel('Rating')
# plt.show()

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