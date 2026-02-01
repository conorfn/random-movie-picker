import csv
import random

# load the csv file of movies

def load_movies(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# filter by ratings

def high_ratings(movies, min_rating=8.0):
    filtered = []
    for movie in movies:
        if float(movie["IMDB_Rating"]) >= min_rating:
            filtered.append(movie)
    return filtered

# generate random movie

def pick_movie(movies):
    movie = random.choice(movies)
    return movie

# main execution

if __name__ == "__main__":
    movies = load_movies("imdb_top_1000.csv")
    high_rated_movies = high_ratings(movies)
    selected_movie = pick_movie(high_rated_movies)
    print(f"Let's watch: {selected_movie['Series_Title']}")