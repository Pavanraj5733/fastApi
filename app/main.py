from fastapi import FastAPI
from app.db.connection import get_database
from app.routes.products import router as products_router  # <-- Add this line

app = FastAPI()
app.include_router(products_router)
# Try to connect to MongoDB at startup
@app.on_event("startup")
def startup_db_client():
    try:
        db = get_database()
        # Try a simple command to check connection
        db.command("ping")
        print("MongoDB connected")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MongoDB app!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)