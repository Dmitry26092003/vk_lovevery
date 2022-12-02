from vkwave.bots.core.dispatching.filters import base, builtin
from vkwave.bots import SimpleBotEvent

from func.group_functions import Group


class WallFilter(base.BaseFilter):
    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)
        if event.object.object.message.attachments:
            return base.FilterResult(event.object.object.message.attachments[0].wall is not None)
        else:
            return base.FilterResult(False)


class CreatorFilter(base.BaseFilter):  # Является ли отправитель сообщения Создателем
    def __init__(self, vk):
        self.vk = vk

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)

        return base.FilterResult(event.object.object.message.from_id in Group.get_creator(self.vk))


class AdminFilter(base.BaseFilter):  # Является ли отправитель сообщения Администратором
    def __init__(self, vk):
        self.vk = vk

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)

        return base.FilterResult(event.object.object.message.from_id in Group.get_admins(self.vk))


class EditorFilter(base.BaseFilter):  # Является ли отправитель сообщения Редактором
    def __init__(self, vk):
        self.vk = vk

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)

        return base.FilterResult(event.object.object.message.from_id in Group.get_editors(self.vk))


class ModeratorFilter(base.BaseFilter):  # Является ли отправитель сообщения Модератором
    def __init__(self, vk):
        self.vk = vk

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)

        return base.FilterResult(event.object.object.message.from_id in Group.get_moderators(self.vk))


class AdvertisersFilter(base.BaseFilter):  # Является ли отправитель сообщения Рекламодателем
    def __init__(self, vk):
        self.vk = vk

    async def check(self, event: SimpleBotEvent) -> base.FilterResult:
        builtin.is_message_event(event)

        return base.FilterResult(event.object.object.message.from_id in Group.get_advertisers(self.vk))

