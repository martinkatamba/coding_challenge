

from typing import List, Optional
from fastapi import APIRouter,HTTPException

from src.schemas import Item, ItemStatus, UserId
from src.utils import add_history
from src import models
from src.dependencies import database


router = APIRouter(
    prefix="/items",  
    tags=["items"],  # Define a tag for documentation purposes
)

@router.get("/")
def read_items( db:database,status: ItemStatus = None )->List[Item]:
    if  status:
        items = db.query(models.Item).filter(models.Item.status==status.value.lower()).all()
    else:
        items = db.query(models.Item).all()
    if len(items)==0:
       raise HTTPException(status_code=404,detail=f"no items found")
    return [Item(**(item.__dict__)) for item in items]

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
