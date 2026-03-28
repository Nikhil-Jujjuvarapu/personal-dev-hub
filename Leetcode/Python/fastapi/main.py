from fastapi import FastAPI, HTTPException

import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/prod")
def create_product(request: schemas.Product):
    db = SessionLocal()

    new_product = models.ProductTable(
        name=request.name,
        age=request.age,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return {
        "message": "Product saved successfully",
        "data": {
            "id": new_product.id,
            "name": new_product.name,
            "age": new_product.age,
        },
    }


@app.get("/prod_details")
def get_det():
    db = SessionLocal()
    products = db.query(models.ProductTable).all()
    db.close()

    return products
@app.get("/product")
def product(id):
    db = SessionLocal()
    product_det = db.query(models.ProductTable).filter(models.ProductTable.id == id).first()
    db.close()
    return product_det


@app.put("/product/{id}")
def update_product(id: int, request: schemas.Product):
    db = SessionLocal()

    product_det = db.query(models.ProductTable).filter(models.ProductTable.id == id).first()

    if product_det is None:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")

    product_det.name = request.name
    product_det.age = request.age

    db.commit()
    db.refresh(product_det)
    db.close()

    return {
        "message": "Product updated successfully",
        "data": {
            "id": product_det.id,
            "name": product_det.name,
            "age": product_det.age,
        },
    }


@app.delete("/product/{id}")
def delete_product(id: int):
    db = SessionLocal()

    product_det = db.query(models.ProductTable).filter(models.ProductTable.id == id).first()

    if product_det is None:
        db.close()
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product_det)
    db.commit()
    db.close()

    return {"message": "Product deleted successfully"}
