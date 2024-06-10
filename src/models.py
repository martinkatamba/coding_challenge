
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from src.database import Base
from src.schemas import ItemStatus
from sqlalchemy.orm import relationship
from datetime import datetime  # Import for default timestamp

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    status = Column(Enum(ItemStatus), default=ItemStatus.NEW)  # Default to NEW
    description = Column(String(50), nullable=True)  # Optional field
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship(User, backref='items')  # Relationship with User

class ItemHistory(Base):
    __tablename__ = "item_history"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'))  # Foreign key to Item.id
    old_assignee = Column(Integer,ForeignKey('users.id'))  # Foreign key to User.id
    old_status = Column(Enum(ItemStatus))  # Default to NEW# Foreign key to User.id
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # Auto-filled timestamp

    item = relationship("Item")  # Relationship with Item model
    new_user = relationship(User, backref='assigned_to_history')  # Relationship with User (new assignee)