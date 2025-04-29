from sqlmodel import SQLModel, Field, create_engine, Session, select, delete
import urllib.parse
from fastapi import FastAPI
import json
# from pydantic import BaseModel

app = FastAPI()




#Step 1: Create a table model:
class Products(SQLModel, table = True):
    id: int | None = Field(default=None,primary_key=True)
    p_name: str
    p_price: float
    p_quantity: int
    p_discount: int
    p_available: bool

#Gather the database details:
database = "Products"
username = urllib.parse.quote_plus("username")
password = urllib.parse.quote_plus("password")
host = "localhost"
port = 5432

#Create the table:
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")
SQLModel.metadata.create_all(engine)

#---------------Our table is created-----------------------------------------

model_mapping = {
    "products": Products,
}

@app.get("/")
async def home(): return {"Page": "Home Page"}

# Creat

async def createProduct(items: str, data: Products):
    model = model_mapping.get(items.lower())
    product = model(**data.model_dump())
    if product.p_quantity > 0: product.p_available = True
    with Session(engine) as session:
        session.add(product)
        session.commit()
    return "Data added successfully"



# Read
@app.get("/read/{table_name}/{id}/")
async def detailsProduct(table_name: str, id: int):
    model = model_mapping.get(table_name.lower())
    with Session(engine) as session:
        if id: statement = select(model).where(model.id == id)
        else: statement = select(model)
        obj = session.exec(statement).first()
    return obj

# Update
@app.patch("/update/{table_name}/{id}/")
async def updateProduct(table_name: str, id: int, data: Products):
    model = model_mapping.get(table_name.lower())
    with Session(engine) as session:
        statement = select(model).where(model.id == id)
        obj = session.exec(statement).first()
        if obj:
            for key, value in data.model_dump(exclude_unset=True).items():
                setattr(obj, key, value)
        if obj.p_quantity > 0:
            obj.p_available = True
        else:
            obj.p_available = False
        session.commit()
        session.refresh(obj)
    return obj

# Delete
@app.delete("/delete/{table_name}/")
async def deleteProduct(table_name: str, id: int | None = None):
    model = model_mapping.get(table_name.lower())
    with Session(engine) as session:
        if id:
            statement = select(model).where(model.id == id)
            obj = session.exec(statement).first()
            session.delete(obj)
            session.commit()
            return f"{obj} removed"
        else:
            statement = delete(model)
            session.exec(statement)
            session.commit()
            return f"All table cleard"


            

