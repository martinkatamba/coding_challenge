

from typing import Optional
from fastapi import APIRouter

from src.schemas import ItemStatus, UserId
from src.utils import add_history
from src import models
from src.dependencies import database


router = APIRouter(
    prefix="/items",  
    tags=["items"],  # Define a tag for documentation purposes
)

@router.get("/{item_id}")
def read_item(item_id: int, db:database,status: Optional[ItemStatus] = None ):
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@router.put("/{item_id}/update")
def change_item_status(item_id: int, status: ItemStatus,db:database):
    
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    old_item_status=item.status#
    item.status = status
    db.add(item)
    db.commit()
    add_history(db=db,
                item_id=item.id,
                item_status=old_item_status,
                old_assignee_id=item.owner_id,
                )

@router.post("/reassign_item/{item_id}/")
def assign_item(item_id: int, new_owner: UserId,db:database):
    
    item = db.query(models.Item).filter(models.Item.id==item_id).first()
    old_assignee_id=item.owner_id#get old asignee id before its modified
    item_status=item.status#
    item.owner_id = new_owner.id
    db.add(item)
    db.commit()
    add_history(db=db,
                item_id=item.id,
                item_status=item_status,
                old_assignee_id=old_assignee_id,
                )
