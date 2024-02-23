from fastapi import APIRouter
from Users import LoginValidator, RegisterValidator, EditUserInfoValidator
from database.userservice import (login_user_db, add_new_user_db, get_all_users_db, get_exact_user_db, delete_user_db,
                                  edit_user_info_db)

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])


@user_router.post('/Registration')
async def registration_user(data: RegisterValidator):
    result = add_new_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользовател с такими данными уже имеется попробуйте снова'}


@user_router.post('/Login')
async def login_user(data: LoginValidator):
    result = login_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в данных попробуйте снова '}


@user_router.get('/All-User')
async def all_user():
    user = get_all_users_db()
    return user


@user_router.get('/Exact-User')
async def exact_user(user_id: int):
    exact_user = get_exact_user_db(user_id=user_id)

    if exact_user:
        return {'message': exact_user}
    else:
        return {'message''Ошибка в данных попробуйте снова'}


@user_router.put('/Edit-User-Info')
async def edit_user_info(data: EditUserInfoValidator):
    result = edit_user_info_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка в id вашего Продукта'}


@user_router.delete('/Delete-User')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь с такими данными не найден'}
