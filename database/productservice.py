from database.models import PhotoProduct, UserProduct, ProductSale
from database import get_db
import datetime

def get_all_product_db():
    db = next(get_db())

    all_product = db.query(ProductSale).all()

    return all_product


def get_exact_product_db(product_id):
    db = next(get_db())
    product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if product:
        return product
    else:
        return 'Такой продукт не найден в вашем аккаунте'


def add_new_product_db(user_id, product_text, product_name, product_price):
    db = next(get_db())
    new_product =  UserProduct(user_id=user_id, product_name=product_name, product_text=product_text,
                              product_price=product_price,
                              )
    db.add(new_product)
    db.commit()

    return (f'Продукт{new_product.product_name} добавлен'
            f'Ваш id -{new_product.product_id}')


def delete_product_db(product_id):
    db = next(get_db())
    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        db.delete(exact_product)
        db.commit()
        return 'Ваш продукт успешно удален'
    else:
        return 'Ваш продукт не найден'


def edit_product_name_db(product_id, new_name):
    db = next(get_db())

    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        exact_product.product_name = new_name
        db.commit()

        return 'Название продукта  успешно изменено'
    else:
        return 'Продукт не найден'


def edit_product_text_db(product_id, new_text):
    db = next(get_db())

    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        exact_product.product_text = new_text
        db.commit()

        return 'Описания продукта  успешно изменено'
    else:
        return 'Продукт не найден'


def edit_product_price_db(product_id, new_price):
    db = next(get_db())
    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        exact_product.product_price = new_price
        db.commit()

        return 'Цена вашего продукта успешно изменена'
    else:
        return 'Продукт не найден'


def edit_product_info_db(product_id, edit_info, new_info):
    db = next(get_db())

    product = get_exact_product_db(product_id)

    if product:
        if edit_info == 'product_name' or 'Product_name':
            product.product_name == new_info
        elif edit_info == 'product_text' or 'Product_text':
            product.product_text == new_info
        elif edit_info == 'product_price' or 'Product_price':
            product.product_price == new_info
        return 'Данные продукта успешно изменены'
    else:
        return 'Продукт не найден'


def like_product_db(product_id):
    db = next(get_db())

    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        exact_product.likes += 1
        db.commit()
        return 'like'
    else:
        return 'Продукт не найден'


def dislike_product_db(product_id):
    db = next(get_db())

    exact_product = db.query(UserProduct).filter_by(product_id=product_id).first()

    if exact_product:
        exact_product.likes -= 1
        db.commit()
        return 'dislike'
    else:
        return 'Продукт не найден'


def upload_product_photo_db(product_id, photo_path):
    db = next(get_db())

    new_photo = PhotoProduct(product_id=product_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()
        return "Фото к Продукту успешно добавленно"
    else:
        return 'Продукт не найден'


def delete_product_photo_db(product_id, photo_path):
    db = next(get_db())

    new_photo = PhotoProduct(product_id=product_id, photo_path=photo_path)

    if new_photo:
        db.delete(new_photo)
        db.commit()
        return 'Фото к Продукту успешно удаленно'
    else:
        return 'Продукт не найден'


def get_all_product_sale_db():
    db = next(get_db())

    all_product_sale = db.query(ProductSale).all()

    return all_product_sale


def get_exact_product_sale_db(sale_id):
    db = next(get_db())

    exact_sale = db.query(ProductSale).filter_by(sale_id=sale_id).first()

    if exact_sale:
        return exact_sale
    else:
        return 'Такая скидка не найденна в вашем аккаунте'


def add_new_product_sale_db(user_id, product_id, sale_from_number, sale_to_number, new_sale_product_price,
                            publish_date=datetime.datetime.now()):
    db = next(get_db())
    new_product_sale = ProductSale(user_id=user_id, product_id=product_id, sale_from_number=sale_from_number,
                                   sale_to_number=sale_to_number, new_sale_product_price=new_sale_product_price,
                                   publish_date=publish_date)
    db.add(new_product_sale)
    db.commit()

    return (f'Скидка добавлена,:'
            f'Ваш id -{new_product_sale.product_id}')


def delete_product_sale_db(product_id, sale_id):
    db = next(get_db())
    exact_product_sale = db.query(ProductSale).filter_by(sale_id=sale_id, product_id=product_id).first()

    if exact_product_sale:
        db.delete(exact_product_sale)
        db.commit()
        return 'Ваша скидка на продукт успешно удалена'
    else:
        return 'Ваша скидка на продукт не найденна'


def edit_product_sale_info_db(sale_id, edit_info, new_info):
    db = next(get_db())

    product_sale = get_exact_product_sale_db(sale_id)

    if product_sale:
        if edit_info == 'sale_from_number' or 'Sale_from_number':
            product_sale.product_name = new_info
        elif edit_info == 'sale_to_number' or 'Sale_to_number':
            product_sale.product_text = new_info
        elif edit_info == 'new_sale_product_price' or 'New_sale_product_price':
            product_sale.product_price = new_info

        return ' Данные скидки успешно изменены'
    else:
        return 'Скидка не найдена'
