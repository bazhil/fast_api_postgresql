from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Item(BaseModel):
    """Serializer"""
    id: int
    name: str
    description: str
    price: int
    on_offer: bool


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

