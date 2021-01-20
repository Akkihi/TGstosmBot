import asyncio

from aiogram.types import Message

import config
from auth import dp
from services.pinterest import pinterest
from services.vk import vk
from utils import permissions


@dp.message_handler(lambda msg: permissions.is_admin(msg.from_user) and not msg.is_command())
async def on_text_message(message: Message):
    # рассылка текстовых сообщений
    for target_channel_id in config.target_channels_ids:
        await message.copy_to(target_channel_id)

    await vk.text_message(message.text)
    pinterest.handle_text(message.text)

    await message.answer('Текстовое сообщение отослано.')
    await asyncio.sleep(1)
