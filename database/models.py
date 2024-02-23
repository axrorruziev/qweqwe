from sqlalchemy import Column, String, DateTime, Date, ForeignKey, Integer, Text, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


class UserProduct(Base):
    __tablename__ = 'user_products'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_name = Column(String)
    product_text = Column(Text)
    product_price = Column(Float)
    likes = Column(Integer, default=0)
    publish_date = Column(DateTime)
    user_fk = relationship(User, lazy='subquery')


class ProductSale(Base):
    __tablename__ = 'product_sale'
    user_id = Column(Integer, ForeignKey('users.user_id'))
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('user_products.product_id'))
    sale_from_number = Column(DateTime)
    sale_to_number = Column(DateTime)
    new_sale_product_price = Column(Float)
    publish_date = Column(String)
    product_fk = relationship(UserProduct, lazy='subquery')


class PhotoProduct(Base):
    __tablename__ = 'photo_product'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('user_products.product_id'))
    photo_path = Column(String)
    product_fk = relationship(UserProduct, lazy='subquery')


class ProductsComment(Base):
    __tablename__ = 'comment_product'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    product_id = Column(Integer, ForeignKey('user_products.product_id'))
    comment_text = Column(Text)
    publish_date = Column(DateTime)
    likes = Column(Integer, default=0)
    profile_photo = Column(String)
    comment_fk = relationship(UserProduct, lazy='subquery')
