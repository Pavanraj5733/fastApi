from pymongo import MongoClient
from fastapi import Depends

def get_database() -> MongoClient:
    client = MongoClient("mongodb+srv://pavan:Pavan123@cluster0.wkzli4o.mongodb.net/")
    return client["test"]  # Replace 'your_database_name' with the actual database name you want to use.