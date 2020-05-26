import json
import pandas as pd
from enum import Enum
from ast import literal_eval
from data_filter import filter_movies

MOVIES = "movies"
CREDITS = "credits"


def parse_movies_from_csv(movies):
    # DEPRECATED — usage only for CSV files.
    for movie in movies:
        movie['budget'] = int(movie['budget'])
        movie['revenue'] = int(movie['revenue'])
        movie['belongs_to_collection'] = literal_eval(
            movie['belongs_to_collection'])
        movie['genres'] = literal_eval(movie['genres'])
        movie['production_companies'] = literal_eval(
            movie['production_companies'])
        movie['production_countries'] = literal_eval(
            movie['production_countries'])
        movie['spoken_languages'] = literal_eval(movie['spoken_languages'])
    return movies


def parse_credits_from_csv(movies_credits):
    # DEPRECATED — usage only for CSV files.
    for credit in movies_credits:
        credit['cast'] = literal_eval(credit['cast'])
        credit['crew'] = literal_eval(credit['crew'])
    return movies_credits


def read_data(file, data_type=MOVIES):
    print('load from {}'.format(file))
    df = pd.read_json(file)
    df = df.dropna()
    if (data_type == MOVIES):
        df = df[df.apply(filter_movies, axis=1)]
    data = df.to_dict('records')

    return data
