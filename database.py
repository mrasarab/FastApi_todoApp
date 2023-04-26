from pymongo import MongoClient
from model import todo

client = MongoClient(
    os.getenv('server_adress'))
database = client.todo_application
collection = database.todos

# Fetch a single todo by title
async def fetch_one_todo(title):
    document = collection.find_one({"title": title})
    return document

# Fetch all todos in the collection
def fetch_all_todos():
    all_todos = []
    cursor = collection.find({})
    for document in cursor:
        all_todos.append(todo(**document))
    return all_todos

# Create a new todo in the collection
def create_todo(todo):
    document = todo
    result = collection.insert_one(document)
    return document

# Update the description of a todo by title
async def update_todo(title, description):
    await collection.update_one({"title": title}, {"$set": {"description": description}})
    document = collection.find_one({"title": title})
    return document

# Remove a todo from the collection by title
async def remove_todo(title):
    await collection.delete_one({"title": title})
    return True
