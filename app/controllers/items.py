from typing import List

from sqlalchemy.orm import Session  # type: ignore

from app.database.models.Item import Item
from app.schemas.item import ItemBase


def get_item_by_id(session: Session, id: str) -> Item:
    return session.query(Item).filter(Item.id == id).first()


def get_items(session: Session, skip: int = 0, limit: int = 100) -> List[Item]:
    return session.query(Item).offset(skip).limit(limit).all()

def create_item(session: Session, item:ItemBase):
    user = Item(name=item.name, price=item.price, id=item.id)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user