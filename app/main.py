
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from sqlalchemy import Column, Integer, String

# Create the FastAPI app
app = FastAPI()

# Define a model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# API endpoints
@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item = Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
