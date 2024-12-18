from typing import Union
from typing import Annotated
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Phrase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    english: str=Field(index=True)
    spanish: str=Field(index=True)
    secret_name:str

sqlite_file_name="database.db"
sqlite_url = f"sqlite:////{sqlite_file_name}"
connect_args = {"check_same_thread":False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]

@app.lifespan("startup")
def on_startup():
    create_db_and_tables
    



@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_price": item.price, "item_id": item_id}