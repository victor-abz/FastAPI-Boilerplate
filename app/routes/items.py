from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore

from app.controllers.items import get_item_by_id, get_items, create_item
from app.database import SessionLocal, engine
from app.schemas.item import ItemBase

router = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.get("/items/", response_model=List[ItemBase])
def read_items(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return get_items(session=session, skip=skip, limit=limit)


@router.get("/items/{id}", response_model=ItemBase)
def read_item(id: str, session: Session = Depends(get_session)):
    item = get_item_by_id(session=session, id=id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/item", response_model=ItemBase)
def create_some_item(item : ItemBase, session: Session = Depends(get_session)):
    return create_item(session=session, item=item)