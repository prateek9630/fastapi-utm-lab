from fastapi import APIRouter
from app.models.schemas import Item

router = APIRouter(prefix="/items", tags=["items"])

fake_db = []

@router.post("/")
def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item added", "item": item}

@router.get("/")
def list_items():
    return fake_db
