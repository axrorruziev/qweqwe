from fastapi import APIRouter, Body, UploadFile

from database.productservice import (get_all_product_db, get_exact_product_db, add_new_product_db, edit_product_name_db,
                                     delete_product_db, like_product_db,
                                     dislike_product_db, upload_product_photo_db, delete_product_photo_db,
                                     edit_product_text_db, edit_product_price_db, edit_product_info_db,
                                     get_all_product_sale_db, get_exact_product_sale_db, edit_product_sale_info_db,
                                     add_new_product_sale_db, delete_product_sale_db)
from product import PublicProductValidator, EditProductValidator, EditProductSaleValidator, NewSaleValidator

product_router = APIRouter(prefix='/prefix', tags=['Работа с Продуктами и Скидками'])


@product_router.post('/Public_Product')
async def public_product(data: PublicProductValidator):
    result = add_new_product_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в данных попробуйте снова'}


@product_router.post('/Edit-Product-Price')
async def edit_product_price(product_id: int, new_price: float):
    result = edit_product_price_db(product_id, new_price)

    if result:
        return {'message': result}
    else:
        return {'message': 'Продукт с такими данными не найден'}


@product_router.post('Like-Product')
async def like_product(product_id: int):
    result = like_product_db(product_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Что=то пошло не так'}


@product_router.post('Dislike-Product')
async def dislike_product(product_id: int):
    result = dislike_product_db(product_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Что=то пошло не так'}


@product_router.post('/Add-Product_photo')
async def add_photo(post_id: int = Body(), photo_path: UploadFile = None):
    with open(f'media/{photo_path.filename}', 'wb') as file:
        user_photo = await photo_path.read()
        file.write(user_photo)

    result = upload_product_photo_db(post_id, f'/gallery/{photo_path.file}')

    if result:
        return {'message': result}
    else:
        return {'message': 'ошибка'}


@product_router.post('/Add-New-Sale')
async def add_new_product_sale(data: NewSaleValidator):
    result = add_new_product_sale_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в данных попробуйте снова'}


@product_router.get('/Get-All-Product')
async def get_all_product():
    result = get_all_product_db()

    return {'message': result}


@product_router.get('/Get-Exact-Product')
async def get_exact_product(product_id):
    result = get_exact_product_db(product_id=product_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'id Продукта не верен попробуйте снова'}


@product_router.get('/Get-All-Product-Sale')
async def get_all_product_sale():
    result = get_all_product_sale_db()

    return {'message': result}


@product_router.get('/Get-Exact-Product-Sale')
async def get_exact_product_sale(sale_id):
    result = get_exact_product_sale_db(sale_id=sale_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'id Скидки не верен попробуйте снова'}


@product_router.put('/Edit-Product-Info')
async def edit_product_info(data: EditProductValidator):
    result = edit_product_info_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в id вашего Продукта'}


@product_router.put('/Edit-Product-Name')
async def edit_product_name(product_id: int, new_name: str):
    result = edit_product_name_db(product_id, new_name)

    if result:
        return {'message': result}
    else:
        return {'message': 'Продукт с такими данными не найден'}


@product_router.put('/Edit-Product_Text')
async def edit_product_text(product_id: int, new_text: str):
    result = edit_product_text_db(product_id, new_text)

    if result:
        return {'message': result}
    else:
        return {'message': 'Продукт с такими данными не найден'}


@product_router.put('/Edit-Product-Sale-Info')
async def edit_product_sale_info(data: EditProductSaleValidator):
    result = edit_product_sale_info_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в id вашего Продукта'}


@product_router.delete('/Delete-Product')
async def delete_product(product_id: int):
    result = delete_product_sale_db(product_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Продукт с такими данными не найден'}


@product_router.delete('Delete-Product-Photo')
async def delete_product_photo(product_id: int, photo_path: str):
    result = delete_product_photo_db(product_id, photo_path)

    if result:
        return {'message': result}
    else:
        return {'message': 'Фото не удалено Ошибка в данных попробуйте снова'}


@product_router.delete('/Delete-Product-Sale')
async def delete_product_sale(sale_id: int):
    result = delete_product_sale_db(sale_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Скидка с такими данными не найдена'}
