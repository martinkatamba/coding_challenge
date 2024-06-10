
from src import models
from src.schemas import ItemCreate, ItemStatus, UserCreate
from sqlalchemy.orm import Session

def create_user(user: UserCreate,db:Session):
    
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    return db_user

def create_user_item(item: ItemCreate, user_id: int,db:Session):
    print(item.dict())
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    return db_item

def add_history(db:Session,item_status:ItemStatus, item_id:int,old_assignee_id: int):
    history_entry = models.ItemHistory(
            item_id = item_id,
            old_status=item_status,
            old_assignee = old_assignee_id,
            )
    db.add(history_entry)
    db.commit()