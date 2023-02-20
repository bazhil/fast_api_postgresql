from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models


app = FastAPI()


class Item(BaseModel):
    """Serializer"""
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True


db = SessionLocal()


@app.get('/')
def index():
    return {'Message': 'Just Another API'}


@app.get('/greet/{name}')
def greet_name(name: str):
    return {'greeting': f'Hello, {name}!'}


@app.get('/greet')
def greet_optional_name(name: Optional[str]='user'):
    return {'Message': f'Hello, {name}'}


@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {'Name': item.name,
            'Description': item.description,
            'Price': item.price,
            'on_offer': item.on_offer}


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()

    return items


@app.get('/item/{item_id}')
def get_an_item(item_id: int):
    pass


@app.post('/items')
def create_an_item():
    pass


@app.put('/item/{item_id}')
def update_an_item(item_id: int):
    pass


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    pass
