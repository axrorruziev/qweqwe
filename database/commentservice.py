from database import get_db
from database.models import ProductsComment

from datetime import datetime


def get_product_comments_db(post_id):
    db = next(get_db())

    post_comments = db.query(ProductsComment).filter_by(post_id=post_id).all()

    if post_comments:
        return post_comments
    else:
        return 'Не получилось взять все отзывы'


def add_comment_db(product_id, comment_text, user_id):
    db = next(get_db())

    new_comment = ProductsComment(post_id=product_id, comment_text=comment_text, user_id=user_id)

    if new_comment:
        db.add(new_comment)
        db.commit()

        return 'Ваш отзыв на этот продукт добавлен'
    else:
        return 'Ваш отзыв не отправился попробуйте заново'


def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(ProductsComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Ваш отзыв на этот продукт успешно удален'
    else:
        return 'Ваш отзыв не удалился попробуйте снова'


def edit_comment_db(comment_id, changed_text):
    db = next(get_db())

    edit_comment = db.query(ProductsComment).filter_by(comment_id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = changed_text
        db.commit()
        return 'Ваш отзыв на этот продукт успешно изменен'
    else:
        return 'Ваш отзыв на этот продукт не изменен!Попробуйте снова'
