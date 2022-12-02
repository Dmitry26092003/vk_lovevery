from config import Settings

from loguru import logger

from vkwave.bots import SimpleLongPollBot, SimpleBotEvent

from CustomFilter import WallFilter, AdminFilter, EditorFilter

import vk_api

from func.bot_functions import Bot

user_token = Settings.user_token
bot_token = Settings.bot_token

bot = SimpleLongPollBot(tokens=bot_token, group_id=217496604)

api = vk_api.VkApi(token=user_token)
vk = api.get_api()


@bot.message_handler((AdminFilter(vk) | EditorFilter(vk)) & WallFilter())
async def repost(event: SimpleBotEvent):
    return Bot.repost(event, vk)


@bot.message_handler((AdminFilter(vk) | EditorFilter(vk)) & bot.text_startswith_filter('https://vk.com/'))
async def repost_all(event: SimpleBotEvent):
    return Bot.repost_all(event, vk)

if __name__ == '__main__':
    bot.run_forever()
