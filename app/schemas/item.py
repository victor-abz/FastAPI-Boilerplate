from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    name: str
    price: int

    class Config:  # to convert non dict obj to json
        orm_mode = True