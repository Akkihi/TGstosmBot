import asyncio
import config
from typing import List
from vkwave.api import Token, BotSyncSingleToken, API
from vkwave.bots import WallPhotoUploader   # PhotoUploader
from vkwave.client import AIOHTTPClient
import os
# from vkwave.bots import SimpleLongPollBot
# from utils.data import data


client: AIOHTTPClient = None
api: API = None
print("started vk images")


async def login(self):
    global client, api
    client = AIOHTTPClient()
    api = API(clients=client, tokens=BotSyncSingleToken(Token(config.VK_TOKEN)))
    print("login(vk)")
    print("GROUP ID IS :  " + config.vk_group_id + "\nTelegram admin: " + str(config.admins_ids))


async def text_message(text: str):
    await api.get_context().wall.post(owner_id=int(config.vk_group_id), message=text)


async def wall_upload(file_path: str, caption: str = None):
    # works only with user token
    photo = await WallPhotoUploader(api.get_context()).get_attachment_from_path(
        group_id=int(config.vk_group_id),
        file_path=file_path
    )
    await api.get_context().wall.post(owner_id=int(config.vk_group_id), message=caption, attachments=photo)
    print("uploaded to vk one")
    await asyncio.sleep(5)
    print("Deleting file: " + file_path)
    os.remove(file_path)


async def wall_uploads(file_paths: List[str], caption: str = None):
    # works only with user token
    photo = await WallPhotoUploader(api.get_context()).get_attachments_from_paths(
        group_id=int(config.vk_group_id),
        file_paths=file_paths
    )
    await api.get_context().wall.post(owner_id=int(config.vk_group_id), message=caption, attachments=photo)
    print("uploaded to vk many")
    await asyncio.sleep(5)
    for file in file_paths:
        print("Deleting file: " + file)
        os.remove(file)


def shutdown(self):
    print("close")
    client.close()


"""def handle_media(file_path: str, caption: str = None):
    pass


def handle_media_group(file_paths: List[str], caption: str = None):
    pass


def handle_text(text: str):
    pass"""
