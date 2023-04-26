from model import todo, person
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_todo, create_todo, update_todo, remove_todo, fetch_all_todos

app = FastAPI()

# Define the origins allowed to access the API
origins = ['https://localhost:3000']

# Add middleware to allow Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "hello"

@app.get("/api/todo")
async def get_todo():
    """
    Retrieve all TODO items.
    """
    try:
        response = fetch_all_todos()
        return response
    except:
        raise HTTPException(404, "something wrong")

@app.get("/api/todo{title}", response_model=todo)
async def get_todo_id(title):
    """
    Retrieve a TODO item by title.
    """
    try:
        response = await fetch_one_todo(title)
        if response:
            return response
        raise HTTPException(
            404, f"there is no TODO item with this title: {title}")
    except:
        raise HTTPException(404, "something wrong")

@app.post("/api/todo", response_model=todo)
def post_todo(todo: todo):
    """
    Create a new TODO item.
    """
    try:
        response = create_todo(todo.dict())
        if response:
            return response
        raise HTTPException(404, "there is no TODO item with this title")
    except:
        raise HTTPException(404, "there is no TODO item with this title")

@app.put("/api/todo{title}", response_model=todo)
async def put_todo(title: str, descrption: str):
    """
    Update an existing TODO item by title.
    """
    try:
        response = await update_todo(title, descrption)
        if response:
            return response
        raise HTTPException(404, f"there is no TODO item with this title: {title}")
    except:
        raise HTTPException(404, f"there is no TODO item with this title: {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    """
    Delete a TODO item by title.
    """
    try:
        response = await remove_todo(title)
        if response:
            return "successfully item deleted"
        raise HTTPException(
            404, f"there is no TODO item with this title: {title}")
    except:
        raise HTTPException(404, f"there is no TODO item with this title: {title}")
