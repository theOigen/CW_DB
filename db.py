from pymongo import MongoClient
import os
from fs import read_data


def connect(db_name="course-work"):
    client = MongoClient("localhost:27017")
    return client[db_name]


def export_collection(db_name="course-work", collection="movies", filepath="./data/movies.json", host="localhost:27017"):
    command = "mongoexport --db {} --collection {} --out {} --host {} --jsonArray".format(
        db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} exported to file {}".format(db_name, collection, filepath)


def import_collection(db_name="course-work", collection="movies", filepath="./data/movies.json", host="localhost:27017"):
    command = "mongoimport --db {} --collection {} --file {} --host {} --jsonArray".format(
        db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} imported from file {}".format(db_name, collection, filepath)


def init_db():
    DB = connect()
    movies = read_data('./data/movies.json')
    movies_credits = read_data('./data/credits.json')
    DB.movies.insert_many(movies)
    DB.credits.insert_many(movies_credits)


if __name__ == '__main__':
    # init_db()
    # print(export_collection(filepath="./data/TEST_MOVIES.json"))
    # print(import_collection(filepath="./data/TEST_MOVIES.json"))
    # print(export_collection(collection="credits",
    #                         filepath="./data/TEST_CREDITS.json"))
    # INIT DB collections from files OR create backup from collection TO files
    # print(import_collection(collection="credits", filepath="./data/credits.json"))
