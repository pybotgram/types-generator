from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class MenuButton(Object):
    """This object describes the bot's menu button in a private chat. It
    should be one of
    - MenuButtonCommands
    - MenuButtonWebApp
    - MenuButtonDefault
    If a menu button other than MenuButtonDefault is set for a
    private chat, then it is applied in the chat. Otherwise the
    default menu button is applied. By default, the menu button opens
    the list of bot commands.
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["MenuButton"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_menu_button: Dict[str, Type["MenuButton"]] = {}
        _type = data.get("")

        if cls is MenuButton and _type in _type_menu_button:
            return _type_menu_button[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class MenuButtonCommands(MenuButton):
    """Represents a menu button, which opens the bot's list of commands.

    Parameters:
        type (``str``):
            Type of the button, must be commands.
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
    ) -> Optional["MenuButtonCommands"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class MenuButtonWebApp(MenuButton):
    """Represents a menu button, which launches a Web App.

    Parameters:
        type (``str``):
            Type of the button, must be web_app.

        text (``str``):
            Text on the button.

        web_app (`~pybotgram.types.WebAppInfo`):
            Description of the Web App that will be launched when the
            user presses the button. The Web App will be able to send
            an arbitrary message on behalf of the user using the
            method answerWebAppQuery.
    """

    def __init__(
        self,
        *,
        type: str,
        text: str,
        web_app: "types.WebAppInfo",
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.text = text
        self.web_app = web_app

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["MenuButtonWebApp"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["web_app"] = types.WebAppInfo._parse(data.get("web_app"), bot)

        return cls(bot=bot, **data)


class MenuButtonDefault(MenuButton):
    """Describes that no specific value for the menu button was set.

    Parameters:
        type (``str``):
            Type of the button, must be default.
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
    ) -> Optional["MenuButtonDefault"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)