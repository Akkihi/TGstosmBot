import asyncio
from typing import List

from aiogram.types import Message, MediaGroup, InputMediaPhoto, InputMediaVideo, InputFile

import config
from services.pinterest import pinterest
from services.vk import vk
from utils import file_format
from utils.data import data


async def send_media_group(message: Message):
    for key in data.keys():
        # Проверка на ошибки в медиагруппе, если один из файлов поступил с ошибкой то мы пропускаем медиагруппу
        if not data[key]['has_error']:
            file_paths = sorted(data[key]['media'])
            caption = data[key]['text']

            # Компоновка файлов в MediaGroup
            target_media_group = files_to_media_group(file_paths, caption)

            # Рассылка по целевым группам
            for target_channel_id in config.target_channels_ids:
                await message.bot.send_media_group(target_channel_id, target_media_group)
                await asyncio.sleep(5)

            # рассылка на другие сервисы
            await vk.wall_uploads(file_paths, caption)
            pinterest.handle_media_group(file_paths, caption)

    data.clear()

    await message.answer('Сообщения отосланы')


def files_to_media_group(file_paths: List[str], caption=None):
    media_group = MediaGroup()

    caption_added = False
    for file_path in file_paths:
        if file_format.is_photo(file_path):
            input_media = InputMediaPhoto(InputFile(file_path))
        elif file_format.is_video(file_path):
            input_media = InputMediaVideo(InputFile(file_path))
        else:
            raise Exception('Unknown file format')

        if caption and not caption_added:
            input_media.caption = caption
            caption_added = True
        media_group.attach(input_media)

    return media_group
