from fastapi import FastAPI

from app.database import initialize_db, users_table, categories_table, messages_table, default_users, default_categories
from app.routers import users, categories, messages


app = FastAPI()
initialize_db()

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(messages.router)


@app.post("/default_data")
def default_data():
    users_table.truncate()
    categories_table.truncate()
    messages_table.truncate()
    users_table.insert_multiple(default_users)
    categories_table.insert_multiple(default_categories)
    return {"message": "Default data has been inserted"}
