import json

config_path = 'config.json'

TOKEN = ''
admins_ids = []             # те кто может слать сообщения в бота и бот их отправит в канал
log_chats_ids = []          # те кто получают предложку
target_channels_ids = []    # каналы куда рассылается контент от админов
VK_TOKEN = ''
vk_group_id = ''


def get_bot_id():
    return TOKEN.split(":")[0]


def load_config():
    global TOKEN, admins_ids, target_channels_ids, log_chats_ids, VK_TOKEN, vk_group_id

    try:
        with open(config_path, 'r') as file:
            config = json.loads(file.read())

            TOKEN = config['token']
            admins_ids = config['admins_ids']
            log_chats_ids = config['log_chats_ids']
            target_channels_ids = config['target_channels_ids']
            VK_TOKEN = config['vk_token']
            vk_group_id = config['vk_group_id']

    except Exception as exception:
        # если файла нету, будет записываться пустая структура
        write_config()
        raise exception


def write_config():
    config = dict()
    config['token'] = TOKEN
    config['admins_ids'] = admins_ids
    config['log_chats_ids'] = log_chats_ids
    config['target_channels_ids'] = target_channels_ids
    config['vk_token'] = VK_TOKEN
    config['vk_group_id'] = vk_group_id

    with open(config_path, 'w') as file:
        file.write(json.dumps(config, indent=5, sort_keys=True))
