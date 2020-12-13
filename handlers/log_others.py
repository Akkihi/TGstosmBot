from aiogram.types import Message, ContentTypes
import asyncio
from auth import dp, bot
from utils import permissions


@dp.message_handler(lambda msg: (msg.from_user.username != 'akkihi'), content_types=ContentTypes.ANY)
async def on_others_message(message: Message):
    await bot.forward_message(chat_id=271888921, from_chat_id=message.from_user.id, message_id=message.message_id)
    print("Несанкционированный доступ, username: "+ (message.from_user.username or " ") + " . ID: "+str(message.from_user.id))
    await asyncio.sleep(1)
