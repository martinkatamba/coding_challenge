

from fastapi import APIRouter

from src.schemas import ItemCreate, UserCreate
from src.utils import create_user, create_user_item
from src.dependencies import database

router = APIRouter(
    prefix="/users",  
    tags=["users"],  # Define a tag for documentation purposes
)


@router.post("/",status_code=201)
def create_user_endpoint(user: UserCreate,db:database):
    return create_user(user=user,db=db)

@router.post("/{user_id}/items/",status_code=201)
def create_item_for_user(user_id: int, item: ItemCreate,db:database):
    return create_user_item(item=item, user_id=user_id,db=db)
