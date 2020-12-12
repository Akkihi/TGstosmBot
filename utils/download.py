import os
from typing import List, Union

from aiogram.types import PhotoSize, Document, Animation, Sticker, Audio, Video
from aiogram.utils.exceptions import BadRequest


async def download_media(media: Union[List[PhotoSize], Document, Animation, Sticker, Audio, Video],
                         custom_file_name=None
                         ) -> str:
    if type(media) is list:
        media = media[-1]

    buffered_writer = None

    for try_count in range(0, 3):
        try:
            buffered_writer = await media.download()
            buffered_writer.close()
            break
        except BadRequest as e:
            if try_count == 2:
                raise e
            print(e)

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
