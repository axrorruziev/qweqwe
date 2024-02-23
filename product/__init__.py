from pydantic import BaseModel
from datetime import datetime


class PublicProductValidator(BaseModel):
    user_id: int
    product_name: str
    product_text: str
    product_price: float



class EditProductValidator(BaseModel):
    product_id: int
    new_name: str
    new_text: str
    new_price: float


class EditProductSaleValidator(BaseModel):
    sale_id: int
    sale_from_number: str
    sale_to_number: str
    new_sale_product_price: str


class NewSaleValidator(BaseModel):
    user_id: int
    product_id: int
    sale_from_number: str
    sale_to_number: str
    new_sale_product_price: str

