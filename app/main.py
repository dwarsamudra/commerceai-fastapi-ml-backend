from fastapi import FastAPI
from app.routes.product_routes import router as product_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CommerceAI")

app.include_router(product_router, prefix="/products", tags=["Products"])

@app.get("/")
def home():
    return {"message": "Welcome to CommerceAI"}