from fastapi import APIRouter
from app.db.connection import get_database

router = APIRouter()

@router.get("/products")
def get_products():
    db = get_database()
    products_collection = db["products"]
    products = list(products_collection.find({}, {"_id": 0}))  # Exclude MongoDB's _id field
    return {"products": products}