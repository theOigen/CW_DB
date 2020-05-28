import json
import pandas as pd
from ast import literal_eval
from data_filter import filter_movies

MOVIES = "movies"
CREDITS = "credits"

json_columns_for_movies = ['genres', 'keywords',
                           'production_countries', 'production_companies', 'spoken_languages']

json_columns_for_credits = ['cast', 'crew']


def read_data(file, data_type=MOVIES):
    print('load from {}'.format(file))
    df = pd.read_json(file)
    if (data_type == MOVIES):
        df['release_date'] = pd.to_datetime(
            df['release_date']).apply(lambda x: x.date())
    df = df.dropna()
    if (data_type == MOVIES):
        df = df[df.apply(filter_movies, axis=1)]
    data = df.to_dict('records')

    return data


def read_csv_data(file, data_type=MOVIES):
    df = pd.read_csv(file)
    if data_type == MOVIES:
        df['release_date'] = pd.to_datetime(
            df['release_date']).apply(lambda x: x.date())
        df = df[df.apply(filter_movies, axis=1)]
        for column in json_columns_for_movies:
            df[column] = df[column].apply(literal_eval)
        return df.to_dict('records')
    elif data_type == CREDITS:
        for column in json_columns_for_credits:
            df[column] = df[column].apply(literal_eval)
        return df.to_dict('records')


def export_csv_to_json():
    movies = read_csv_data('./data_files/tmdb_5000_movies.csv')
    movies_credits = read_csv_data('./data_files/tmdb_5000_credits.csv', CREDITS)
    with open('./data_files/tmdb_movies.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(movies, indent=4, sort_keys=True, default=str))
    with open('./data_files/tmdb_credits.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(movies_credits, indent=4, sort_keys=True, default=str))