import os
from typing import List, Union

from aiogram.types import PhotoSize, Document, Animation, Sticker, Audio, Video


async def download_media(media: Union[List[PhotoSize], Document, Animation, Sticker, Audio, Video],
                         custom_file_name=None
                         ) -> str:
    if type(media) is list:
        media = media[-1]

    buffered_writer = await media.download()
    buffered_writer.close()
    file_path = buffered_writer.name

    file_ext = file_path.split('.')[-1]

    if custom_file_name:
        custom_file_name_path = os.path.dirname(file_path) + \
                          os.path.sep + \
                          str(custom_file_name) + \
                          '.' + \
                          file_ext
        os.rename(file_path, custom_file_name_path)
        return custom_file_name_path
    else:
        return file_path
