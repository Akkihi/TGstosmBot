from aiogram.types import User
from aiogram.utils.markdown import text, link


def get_full_name(user: User):
    return (user.first_name or '') + ' ' + (user.last_name or '')


def get_user_link(user: User):
    return link(get_full_name(user), 'tg://user?id=' + str(user.id))
