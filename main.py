from fastapi import Depends, FastAPI
from model import product
from database import SessionLocal,engine
import database_model
from sqlalchemy.orm import sessionmaker

database_model.Base.metadata.create_all(bind=engine)

app = FastAPI() 



@app.get('/')
def greet():
    return 'welcome to telusko trac'

Products = [
    product(id=1,name='phone', description='Smartphone', price=699.99, quantity=50),
    product(id=2, name='laptop', description='gaming laptop', price=999.99, quantity=30),
    product(id=5, name='pen', description='A blue ink pen',price=1.99,quantity=100),
    product(id=6, name='Table',description='A wooden table', price=199.99, quantity=20)
]

def get_db():
    db = SessionLocal()
    count = db.query(database_model.Product).count()
    try:
      yield db
    finally:  
      db.close()

def init_db():
    db =SessionLocal()

    count = 0

    if count ==0:
        for product in Products:
         db.add(database_model.Product(**product.model_dump()))
        db.commit() 

init_db() 

@app.get('/products')
def get_all_products(db: SessionLocal =Depends(get_db)):

    db_products =db.query(database_model.Product).all()
    return db_Products

@app.get('/products/{id}') 
def get_products_by_id(id: int, db:Session = Depends(get_db)):
   db_product = db.query(database_model.product).filter(database_model.product.id==id).first()
    for product in product:
        if product.id ==id:
         return product
    
 
    return 'product not found' 
      


@app.post('/product')
def add_product(products:product,db:session = Depends(get_db)):
    db.add(database_model.product(**product.model_dump()))
    db.commit()
    
    return product

@app.put('/product')
def update_product(id:int, product:product):
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





