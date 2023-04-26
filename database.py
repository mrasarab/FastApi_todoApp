from pymongo import MongoClient
from model import todo

client = MongoClient(
    os.getenv('server_adress'))
database = client.todo_application
collection = database.todos


async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document


def fetch_all_todos():
    all_todos = []
    cursor = collection.find({})
    for document in cursor:
        all_todos.append(todo(**document))
    return all_todos


def create_todo(todo):
    document = todo
    result = collection.insert_one(document)
    return document


async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = collection.find_one({"title": title})
    return document


async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True


