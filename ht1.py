import pandas as pd

movies = pd.read_csv("./movies.csv", encoding="latin1")

print(
  "\nLos datos tienen", len(movies), "observaciones y", len(movies.columns), "variables."
)
#4.1
movies.nlargest(10, 'budget')['title']
#4.2
movies.nlargest(10, 'revenue')['title']
#4.3
movies.nlargest(1, 'voteCount')['title']
#4.4
movies.nsmallest(1, 'voteAvg')['title']