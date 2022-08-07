from typing import Any, Dict, Type, Union, Optional

import pybotgram
from .object import Object


class BotCommandScope(Object):
    """This object represents the scope to which bot commands are applied.
    Currently, the following 7 scopes are supported:
    - :obj:`~pybotgram.types.BotCommandScopeDefault`
    - :obj:`~pybotgram.types.BotCommandScopeAllPrivateChats`
    - :obj:`~pybotgram.types.BotCommandScopeAllGroupChats`
    - :obj:`~pybotgram.types.BotCommandScopeAllChatAdministrators`
    - :obj:`~pybotgram.types.BotCommandScopeChat`
    - :obj:`~pybotgram.types.BotCommandScopeChatAdministrators`
    - :obj:`~pybotgram.types.BotCommandScopeChatMember`
    """

    def __init__(self, type: str, **_kwargs: Any):
        super().__init__()

        self.type = type

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["BotCommandScope"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        bot_command_type = data.get("type")
        mapping = {
            "default": BotCommandScopeDefault,
            "all_private_chats": BotCommandScopeAllPrivateChats,
            "all_group_chats": BotCommandScopeAllGroupChats,
            "all_chat_administrators": BotCommandScopeAllChatAdministrators,
            "chat_administrators": BotCommandScopeChatAdministrators,
            "chat_member": BotCommandScopeChatMember
        }

        if bot_command_type in mapping and cls is BotCommandScope:
            return mapping[bot_command_type]._parse(data, bot)

        else:
            return cls(**data, bot=bot)


class BotCommandScopeDefault(BotCommandScope):
    """Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the
    user.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__(type="default")


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """Represents the scope of bot commands, covering all private chats.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__(type="all_private_chats")


class BotCommandScopeAllGroupChats(BotCommandScope):
    """Represents the scope of bot commands, covering all group and
    supergroup chats.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__(type="all_group_chats")


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all group and
    supergroup chat administrators.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__(commands="all_chat_administrators")


class BotCommandScopeChat(BotCommandScope):
    """Represents the scope of bot commands, covering a specific chat.

    Parameters:
        chat_id (:py:obj:`int` | :py:obj:`str`):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).
    """

    def __init__(self, *, chat_id: Union[int, str], **_kwargs: Any):
        super().__init__(type="chat")
        
        self.chat_id = chat_id


class BotCommandScopeChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all administrators of a
    specific group or supergroup chat.

    Parameters:
        chat_id (:py:obj:`int` | :py:obj:`str`):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).
    """

    def __init__(self, *, chat_id: Union[int, str], **_kwargs: Any):
        super().__init__(type="chat_administrators")
        
        self.chat_id = chat_id


class BotCommandScopeChatMember(BotCommandScope):
    """Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat.

    Parameters:
        chat_id (:py:obj:`int` | :py:obj:`str`):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).

        user_id (:py:obj:`int`):
            Unique identifier of the target user.
    """

    def __init__(self, *, chat_id: Union[int, str], user_id: int, **_kwargs: Any):
        super().__init__(type="chat_member")
        
        self.chat_id = chat_id
        self.user_id = user_id