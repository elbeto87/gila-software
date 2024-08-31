from fastapi import FastAPI

app = FastAPI()

users = []
messages = []


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/send_message")
def send_message(category: str, message: str):
    return {"category": category, "message": message}


@app.post("/register_user")
def register_user(username: str, email: str, category: str):
    return {"username": username, "email": email, "category": category}
