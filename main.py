from fastapi import FastAPI
from model import Product
app = FastAPI() 
@app.get('/')
def greet():
    return 'welcome to telusko trac'

Products = [
    Product(id=1,name='phone', description='Smartphone', price=699.99, quantity=50),
    Product(id=2, name='laptop', description='gaming laptop', price=999.99, quantity=30),
    Product(id=5, name='pen', description='A blue ink pen',price=1.99,quantity=100),
    Product(id=6, name='Table',description='A wooden table', price=199.99, quantity=20)
]
@app.get('/products')
def get_products():
    return Products

@app.get('/products/{id}') 
def get_products_by_id(id: int):
    for product in product:
        if product.id ==id:
         return product
    
 
    return 'product not found' 
      


@app.post('/product')
def add_product(products:Product):
    Products.append(Product)
    return Product

@app.put('/product')
def update_product(id:int, product:Product):
    for i in range (len(product)):
        if product[i].id ==id:
            product[i] = product
            return 'prodcut Added successfully'   

    return 'no product found'


@app.delete('/product')
def delete_product(id: int):
    for i in range (len(product)):
        if product [i].id ==id:
            del product[i]
            return 'product Deleted succesfully'


            return 'no product found'





