from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# Root endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Get endpoint with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Post endpoint with request body
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}