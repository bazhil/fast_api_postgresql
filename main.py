from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'Message': 'Just Another API'}


@app.get('/greet/{name}')
def greet_name(name: str):
    return {'greeting': f'Hello, {name}!'}

