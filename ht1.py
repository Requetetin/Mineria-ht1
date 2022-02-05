import pandas as pd

movies = pd.read_csv("./movies.csv", encoding="latin1")

#??
print("\nLos datos tienen", len(movies), "observaciones y", len(movies.columns), "variables.")

#------------------ Preguntas ------------------
#4.1 mas presupuesto
budget = movies.nlargest(10, ['budget'])[['title', 'genres', 'budget', 'revenue']]
print("Las 10 peliculas con mas presupuestos fueron \n", budget)
#4.2
revenues = movies.nlargest(10, 'revenue')[['title', 'revenue']]
print("Las 10 peliculas con mas ingresos fueron \n", revenues)
#4.3
mostVoted = movies.nlargest(5, 'voteCount')[['title', 'voteCount', 'voteAvg']]
print("La pelicula con mas votos fue: \n", mostVoted)
#4.4
worst = movies.nsmallest(1, 'voteAvg')[['title', 'genres', 'voteAvg']]
print("La peor pelicula segun los votos de los usuarios es:  \n", worst)
#4.5
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
yearly = movies['releaseDate'].dt.year.value_counts()
yearly.plot.bar()
#4.6
#a
movies['mainGenre'].sort_values(by=['dateReleased'])
#b
movies['mainGenre'] = movies['genres'].str.split('|', n=-1).str[0]
movies['mainGenre'].value_counts().plot.bar()

#4.12
movies['month'] = movies['releaseDate'].dt.month
movies.sort_values('revenue', ascending=False)[['title', 'revenue', 'month']].head(20

#4.13
movies['releaseDate'] = pd.to_datetime(movies['releaseDate'])
yearly = movies['releaseDate'].dt.month.value_counts()
yearly.plot.bar())