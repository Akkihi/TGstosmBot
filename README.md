# TGstosmBot
Telegram-bot sending content to others social media

## Supports platforms
* Telegram
* VKontakte

## Features
* Send content from bot to social media
* Send content from other users to admins, works like feedback bot

### Specific
* Supports order of media_group
* Works asynchronously

### TODO
* User profile links from suggested content (Vk.cc & telegram text formats)
* Suggested content from vk into telegram bot (with links vk profile)
* Optimization vk structure

## Installation
1. ```pip3 install -r requirements.txt```
2. ```python3 run.py``` for generating config.json file   
3. Add your tokens to config.json   
4. Add admins and target channel to config.json
5. Add bot as admin to target telegram channel
6. Add bot as admin to Vk channel
7. ```python3 run.py```

Now bot is ready to work!
