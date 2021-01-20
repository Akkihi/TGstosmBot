import asyncio

from aiogram.types import Message, ContentType
from aiogram.utils.exceptions import BadRequest

from auth import dp, runner
from utils import permissions, download
from utils.data import data
from .command_handlers.send_media_group import send_media_group


@dp.message_handler(lambda msg: not permissions.is_admin(msg.from_user) and
                                not permissions.is_log_target(msg.from_user) and
                                not msg.is_command() and
                                msg.media_group_id,
                    content_types=[ContentType.PHOTO, ContentType.VIDEO])
async def log_media_group(message: Message):
    # Инициализация словаря под медиагруппу если ее еще нет в списке
    if message.media_group_id not in data.keys():
        data[message.media_group_id] = dict()
        data[message.media_group_id]['media'] = list()
        data[message.media_group_id]['text'] = None
        data[message.media_group_id]['schedule_task'] = None
        data[message.media_group_id]['has_error'] = False
        data[message.media_group_id]['from_user'] = message.from_user

    if data[message.media_group_id]['has_error']:
        print('Пропуск сообщения {} по причине ошибки в медиа-группе'.format(message.message_id))
        return

    # Генерация имени файла
    custom_file_name = str(message.media_group_id) + '_' + str(message.message_id)

    # Скачивание файла
    try:
        file_path = await download.download_media(message.photo or message.video,
                                                  custom_file_name=custom_file_name)
    except BadRequest as e:
        await message.reply('Произошла ошибка скачивания сообщения, попробуйте еще раз')
        data[message.media_group_id]['has_error'] = True
        return

    # Сохранение файла в список
    data[message.media_group_id]['media'].append(file_path)

    # Установка таймера на отправку медиагруппы
    if data[message.media_group_id]['schedule_task']:
        data[message.media_group_id]['schedule_task'].cancel()
    task = runner.loop.call_later(20, asyncio.ensure_future, send_media_group(message))
    data[message.media_group_id]['schedule_task'] = task

    # Сохранение подписи к изображению
    if message.caption and len(message.caption) > 0:
        data[message.media_group_id]['text'] = message.caption

    await asyncio.sleep(1)
