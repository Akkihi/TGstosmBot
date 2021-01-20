import asyncio

from aiogram.types import Message, ContentTypes, ParseMode
from aiogram.utils.markdown import text

import config
from auth import dp
from utils import permissions, user_tools


@dp.message_handler(lambda msg: not permissions.is_admin(msg.from_user) and
                                not permissions.is_log_target(msg.from_user) and
                                not msg.is_command() and
                                not msg.media_group_id,
                    content_types=ContentTypes.ANY)
async def on_any_message(message: Message):
    # Пересылка предложки админам
    for log_chat_id in config.log_chats_ids:
        await message.forward(log_chat_id)

        from_user_caption = text('Предложка от пользователя: ', user_tools.get_user_link(message.from_user))
        await message.bot.send_message(log_chat_id, from_user_caption, parse_mode=ParseMode.MARKDOWN_V2)

        await asyncio.sleep(1)

    print("Предложка от username: " + (message.from_user.username or " ") + " . ID: " + str(message.from_user.id))
    await asyncio.sleep(1)
    await message.answer('Сообщение отослано')
