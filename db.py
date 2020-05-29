from pymongo import MongoClient
import os
from fs import read_data, CREDITS


def connect(db_name="course-work"):
    client = MongoClient("localhost:27017")
    return client[db_name]


def export_collection(db_name="course-work", collection="movies", filepath="./data_files/tmdb_movies.json", host="localhost:27017"):
    command = "mongoexport --db {} --collection {} --out {} --host {} --jsonArray".format(
        db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} exported to file {}".format(db_name, collection, filepath)


def import_collection(db_name="course-work", collection="movies", filepath="./data_files/tmdb_movies.json", host="localhost:27017"):
    command = "mongoimport --db {} --collection {} --file {} --host {} --jsonArray".format(
        db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} imported from file {}".format(db_name, collection, filepath)


def init_db():
    DB = connect()
    movies = read_data('./data_files/tmdb_movies.json')
    movies_credits = read_data(
        './data_files/tmdb_credits.json', data_type=CREDITS)
    DB.movies.insert_many(movies)
    DB.credits.insert_many(movies_credits)


if __name__ == '__main__':
    init_db()
