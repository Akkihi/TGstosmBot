import asyncio

from aiogram.types import Message, ContentTypes

import config
from auth import dp
from utils import permissions


@dp.message_handler(lambda msg: not permissions.is_admin(msg.from_user) and
                                not permissions.is_log_target(msg.from_user) and
                                not msg.is_command(),
                    content_types=ContentTypes.ANY)
async def on_others_message(message: Message):
    # Пересылка предложки админам
    for log_chat_id in config.log_chats_ids:
        await message.forward(log_chat_id)
        await asyncio.sleep(1)
    print("Предложка от username: " + (message.from_user.username or " ") + " . ID: " + str(message.from_user.id))
    await asyncio.sleep(1)
