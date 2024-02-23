from fastapi import FastAPI

from Users.userapi import user_router
from product.productapi import product_router

from database import Base, engine
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(product_router)

