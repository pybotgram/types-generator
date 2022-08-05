from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class BotCommandScope(Object):
    """This object represents the scope to which bot commands are applied.
    Currently, the following 7 scopes are supported:
    - BotCommandScopeDefault
    - BotCommandScopeAllPrivateChats
    - BotCommandScopeAllGroupChats
    - BotCommandScopeAllChatAdministrators
    - BotCommandScopeChat
    - BotCommandScopeChatAdministrators
    - BotCommandScopeChatMember
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["BotCommandScope"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_bot_command_scope: Dict[str, Type["BotCommandScope"]] = {}
        _type = data.get("")

        if cls is BotCommandScope and _type in _type_bot_command_scope:
            return _type_bot_command_scope[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class BotCommandScopeDefault(BotCommandScope):
    """Represents the default scope of bot commands. Default commands are
    used if no commands with a narrower scope are specified for the
    user.

    Parameters:
        type (``str``):
            Scope type, must be default.
    """

    def __init__(
        self,
        *,
        type: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeDefault"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """Represents the scope of bot commands, covering all private chats.

    Parameters:
        type (``str``):
            Scope type, must be all_private_chats.
    """

    def __init__(
        self,
        *,
        type: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeAllPrivateChats"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeAllGroupChats(BotCommandScope):
    """Represents the scope of bot commands, covering all group and
    supergroup chats.

    Parameters:
        type (``str``):
            Scope type, must be all_group_chats.
    """

    def __init__(
        self,
        *,
        type: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeAllGroupChats"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all group and
    supergroup chat administrators.

    Parameters:
        type (``str``):
            Scope type, must be all_chat_administrators.
    """

    def __init__(
        self,
        *,
        type: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeAllChatAdministrators"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeChat(BotCommandScope):
    """Represents the scope of bot commands, covering a specific chat.

    Parameters:
        type (``str``):
            Scope type, must be chat.

        chat_id (``int`` | ``str``):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).
    """

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.chat_id = chat_id

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeChat"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeChatAdministrators(BotCommandScope):
    """Represents the scope of bot commands, covering all administrators of a
    specific group or supergroup chat.

    Parameters:
        type (``str``):
            Scope type, must be chat_administrators.

        chat_id (``int`` | ``str``):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).
    """

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.chat_id = chat_id

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeChatAdministrators"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class BotCommandScopeChatMember(BotCommandScope):
    """Represents the scope of bot commands, covering a specific member of a
    group or supergroup chat.

    Parameters:
        type (``str``):
            Scope type, must be chat_member.

        chat_id (``int`` | ``str``):
            Unique identifier for the target chat or username of the
            target supergroup (in the format @supergroupusername).

        user_id (``int``):
            Unique identifier of the target user.
    """

    def __init__(
        self,
        *,
        type: str,
        chat_id: Union[int, str],
        user_id: int,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["BotCommandScopeChatMember"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)