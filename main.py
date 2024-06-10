
from fastapi import FastAPI

from src.dependencies import set_up_migrations
from routes import users, items

app = FastAPI()

set_up_migrations()


@app.get("/")
async def index():
     return {"msg": "service running ....."}

# Include routers (endpoints) in your application
app.include_router(users.router)
app.include_router(items.router)

