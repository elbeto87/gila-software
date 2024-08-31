from fastapi import FastAPI

from app.models import UserRegistration

app = FastAPI()

users = []
messages = []


@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/send_message")
def send_message(category: str, message: str):
    return {"category": category, "message": message}


@app.post("/register_user")
def register_user(user: UserRegistration):
    users.append({"username": user.username, "category": user.categories})
    return {"username": user.username, "category": user.categories}
