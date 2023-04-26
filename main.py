from model import todo,person
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import fetch_one_todo, create_todo, update_todo, remove_todo, fetch_all_todos
app = FastAPI()

origins = ['https://localhost:3000']

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
    try:
        response = fetch_all_todos()
        return response
    except:
        raise HTTPException(404, "something wrong")


@app.get("/api/todo{title}", response_model=todo)
async def get_todo_id(title):
    try:
        response = await fetch_one_todo(title)
        if response:
            return response
        raise HTTPException(
        404, f"there is no TODO item with this title : {title}")
    except:
        raise HTTPException(404, "something wrong")

@app.post("/api/todo", response_model=todo)
def post_todo(todo: todo):
    try:
        response = create_todo(todo.dict())
        if response:
            return response
        raise HTTPException(404, "there is no TODO item with this title")
    except:
        raise HTTPException(404, "there is no TODO item with this title")


@app.put("/api/todo{title}", response_model=todo)
async def put_todo(title: str, descrption: str):
    try:
        response = await update_todo(title, descrption)
        if response:
            return response
        raise HTTPException(404, f"there is no TODO item with this title : {title}")
    except:
        raise HTTPException(404, f"there is no TODO item with this title : {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    try:
        response = await remove_todo(title)
        if response:
            return "successfully item deleted"
        raise HTTPException(
        404, f"there is no TODO item with this title : {title}")
    except:
        raise HTTPException(404, f"there is no TODO item with this title : {title}")
