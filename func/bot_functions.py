from random import randint
from time import sleep

from func.group_functions import Group

from vk_api.vk_api import VkApiMethod
from vkwave.bots import SimpleBotEvent
from vk_api.exceptions import *


class Bot:
    @staticmethod
    def repost(event: SimpleBotEvent, vk: VkApiMethod):
        result = Group.repost(vk,
                              object=f'wall{event.object.object.message.attachments[0].wall.from_id}_{event.object.object.message.attachments[0].wall.id}')
        return f'{result["success"]=}, {result["post_id"]=}, {result["reposts_count"]=}, {result["likes_count"]=}'

    @staticmethod
    def repost_all(event: SimpleBotEvent, vk: VkApiMethod):
        url = event.object.object.message.text
        domain = url.split('/')[-1]
        try:
            vk.groups.getById(group_id=domain)
        except ApiError as err:
            print(err)
            return 'Не Валидная ссылка'
        o = 105
        aaa = True
        while aaa:
            aaa = list(
                map(
                    lambda x: f'wall{x["copy_history"][0]["owner_id"]}_{x["copy_history"][0]["id"]}',
                    filter(
                        lambda f: 'copy_history' in f.keys(),
                        vk.wall.get(domain='shop_for_busy_people', count=100, offset=o)["items"]
                    )
                )
            )
            print(aaa)
            for a in aaa:
                print(a)
                r = randint(5, 40)
                print(r)
                try:
                    result = Group.repost(
                        vk,
                        object=a
                    )
                except Captcha:
                    return 'Error Captcha'
                sleep(r)
            o += 100
        return 'Complete'
