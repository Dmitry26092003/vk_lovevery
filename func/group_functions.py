from loguru import logger

from vk_api.vk_api import VkApiMethod

from config import Settings


class Group:
    @staticmethod
    def get_managers_dict_list(vk: VkApiMethod) -> list[dict]:
        result = vk.groups.getMembers(
            group_id=Settings.group_id,
            filter='managers'
        )['items']

        logger.debug(f'Запрошен список Руководиделей группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def get_creator(vk: VkApiMethod) -> int:
        result = list(
            filter(
                lambda f: f['role'] == 'creator',
                Group.get_managers_dict_list(vk)
            )
        )[0]['id']

        logger.debug(f'Запрошен ID Создателя группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def get_admins(vk: VkApiMethod) -> list[int]:
        result = list(
            map(
                lambda x: x['id'],
                filter(
                    lambda f: f['role'] == 'administrator',
                    Group.get_managers_dict_list(vk)
                )
            )
        )

        logger.debug(f'Запрошены ID Администраторов группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def get_editors(vk: VkApiMethod) -> list[int]:
        result = list(
            map(
                lambda x: x['id'],
                filter(
                    lambda f: f['role'] == 'editor',
                    Group.get_managers_dict_list(vk)
                )
            )
        )

        logger.debug(f'Запрошены ID Редакторов группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def get_moderators(vk: VkApiMethod) -> list[int]:
        result = list(
            map(
                lambda x: x['id'],
                filter(
                    lambda f: f['role'] == 'moderator',
                    Group.get_managers_dict_list(vk)
                )
            )
        )

        logger.debug(f'Запрошены ID Модераторов группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def get_advertisers(vk: VkApiMethod) -> list[int]:
        result = list(
            map(
                lambda x: x['id'],
                filter(
                    lambda f: f['role'] == 'advertiser',
                    Group.get_managers_dict_list(vk)
                )
            )
        )

        logger.debug(f'Запрошены ID Рекламодателей группы {Settings.group_id}. Результат: \n{result}')
        return result

    @staticmethod
    def repost(vk, object):
        result = vk.wall.repost(
            object=object,
            group_id=Settings.group_id
        )

        return result
