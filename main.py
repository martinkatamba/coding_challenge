from typing import Optional
from fastapi import FastAPI

from src.dependencies import set_up_migrations
from src.schemas import ItemCreate, ItemStatus, UserCreate, UserId
from src.dependencies import database
from src.utils import add_history, create_user, create_user_item
from src import models
from routes import users, items

app = FastAPI()

set_up_migrations()


@app.get("/")
async def index():
     return {"msg": "service running ....."}

# Include routers (endpoints) in your application
app.include_router(users.router)
app.include_router(items.router)

