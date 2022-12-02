import vk_api

from config import Settings

from func.group_functions import Group

user_token = Settings.user_token
bot_token = Settings.bot_token

api = vk_api.VkApi(token=user_token)
vk = api.get_api()

o = 1
while True:
    aaa = vk.wall.get(domain='shop_for_busy_people', count=100, offset=o)["items"]
    o += 100
    print(aaa[0]['copy_history'][0]['owner_id'], aaa[0]['copy_history'][0]['id'])
    print()
    print(aaa[-1]['copy_history'][0]['owner_id'], aaa[0]['copy_history'][0]['id'])
    print()


# vk.wall.repost(object='wall-217005029_3', group_id=217496604, message='test wall')
