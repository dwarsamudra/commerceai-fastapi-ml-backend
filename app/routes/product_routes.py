from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse
from app.ml.model import predict_price

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.get("/predict-price/")
def get_predicted_price(name: str):
    price = predict_price(name)
    return {"product": name, "predicted_price": price}


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == product_id).first()

    if not existing_product:
        return {"error": "Product not found"}

    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.description = product.description

    db.commit()
    db.refresh(existing_product)
    return existing_product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}
