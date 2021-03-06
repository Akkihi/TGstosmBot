from aiogram.types import User

import config


def is_admin(user: User) -> bool:
    if user.id in config.admins_ids:
        return True


def is_log_target(user: User) -> bool:
    if user.id in config.log_chats_ids:
        return True
