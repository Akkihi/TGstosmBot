from aiogram.types import Message, ContentTypes
import asyncio
from auth import dp, bot
from utils import permissions


@dp.message_handler(lambda msg: (msg.from_user.username != 'akkihi'), content_types=ContentTypes.ANY)
async def on_others_message(message: Message):
    await bot.send_message(chat_id=271888921, text="Несанкционированный доступ!"+"\nОт пользователя: "+ (message.from_user.username or "") + "\nC именем: "+ (message.from_user.full_name or " ") +"\nID:" + str(message.from_user.id))
    await message.copy_to(chat_id=271888921)
    print("Несанкционированный доступ, username: "+ (message.from_user.username or " ") + " . ID: "+str(message.from_user.id))
    await asyncio.sleep(1)
