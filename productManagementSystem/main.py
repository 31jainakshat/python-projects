from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")

def greet():
    return "Welcome to Product Management System"

products = [Product(id=1, name="phone", description="new iphone", price=600000, quantity=3),
            Product(id=2, name="laptop", description="gaming laptop", price=750000, quantity=2),
            Product(id=3, name="headphones", description="wireless noise-cancelling", price=20000, quantity=10),
            Product(id=4, name="smartwatch", description="fitness tracker", price=15000, quantity=8),
            Product(id=5, name="tablet", description="10-inch display", price=30000, quantity=5),
            Product(id=6, name="camera", description="mirrorless digital camera", price=45000, quantity=4),
            Product(id=7, name="speaker", description="bluetooth portable speaker", price=8000, quantity=12),
            Product(id=8, name="keyboard", description="mechanical gaming keyboard", price=7000, quantity=7)]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for p in products:
        if p.id == id:
            return p
    return f"product with id {id} not found!"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if id == products[i].id:
            products[i] = product
            return "Product updated successfully"
    return f"Couldn't found the product with id {id}"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if id == products[i].id:
            del products[i]
            return "Product deleted successfully"
    return f"Couldn't delete the product with id {id} as the produc not found!"