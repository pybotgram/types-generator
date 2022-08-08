from typing import Any, Dict, Type, Optional

import pybotgram
from .object import Object
from pybotgram import types


class MenuButton(Object):
    """This object describes the bot's menu button in a private chat. It
    should be one of
    - :obj:`~pybotgram.types.MenuButtonCommands`
    - :obj:`~pybotgram.types.MenuButtonWebApp`
    - :obj:`~pybotgram.types.MenuButtonDefault`

    If a menu button other than MenuButtonDefault is set for a
    private chat, then it is applied in the chat. Otherwise the
    default menu button is applied. By default, the menu button opens
    the list of bot commands.
    """

    def __init__(self, type: str, **_kwargs: Any):
        super().__init__()

        self.type = type

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["MenuButton"]]:
        if not (isinstance(data, dict) and data):
            return None

        menu_button_type = data.get("type")
        mapping = {
            "commands": MenuButtonCommands,
            "web_app": MenuButtonWebApp,
            "default": MenuButtonDefault,
        }

        if menu_button_type in mapping and cls is MenuButton:
            return mapping[menu_button_type]._parse(data, bot)

        else:
            return cls(**data, bot=bot)


class MenuButtonCommands(MenuButton):
    """Represents a menu button, which opens the bot's list of commands."""

    def __init__(self, **_kwargs: Any):
        super().__init__(type="commands")


class MenuButtonWebApp(MenuButton):
    """Represents a menu button, which launches a Web App.

    Parameters:
        text (:obj:`str`):
            Text on the button.

        web_app (:obj:`~pybotgram.types.WebAppInfo`):
            Description of the Web App that will be launched when the
            user presses the button. The Web App will be able to send
            an arbitrary message on behalf of the user using the
            method answerWebAppQuery.
    """

    def __init__(
        self, *, text: str, web_app: "types.WebAppInfo", **_kwargs: Any
    ):
        super().__init__(type="web_app")

        self.text = text
        self.web_app = web_app


class MenuButtonDefault(MenuButton):
    """Describes that no specific value for the menu button was set."""

    def __init__(self, **_kwargs: Any):
        super().__init__(type="default")
