import pandas as pd

movies = pd.read_csv("./movies.csv", encoding="latin1")

print(
  "\nLos datos tienen", len(movies), "observaciones y", len(movies.columns), "variables."
)

print(movies.describe())
print("\n\n\n")
print(movies.head())