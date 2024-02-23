from database.models import User

from database import get_db


def get_all_users_db():
    db = next(get_db())

    all_user = db.query(User).all()

    return all_user


def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'Такой пользователь не найден'


def add_new_user_db(name, surname, phone_number, city, password):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return 'Такой пользователь уже зарегестрирован'
    else:
        new_user = User(name=name, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()

        return (f'Новый пользователь {new_user.name} успешно зарегестрирован',
                f'Ваш id {new_user.user_id}')


def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if not user:
        return 'Такой пользователь найден'
    else:
        db.delete(user)
        db.commit()
        return 'Пользователь успешно удален'


def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'name' or 'Name':
            exact_user.name = new_info
        elif edit_info == 'city' or 'City':
            exact_user.city = new_info
        elif edit_info == 'password' or 'Password':
            exact_user.password = new_info
        elif edit_info == 'phone_number' or 'Phone_number':
            exact_user.phone_number = new_info

        db.commit()

        return 'Даннные пользователя успешно изменены'
    else:
        return 'Данные пользователя не изменены по причине(Пользователь не найден)'


def login_user_db(phone_number, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    else:
        return 'Ошибка в данных'
