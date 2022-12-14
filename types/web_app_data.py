from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class WebAppData(Object):
    """Describes data sent from a Web App to the bot.

    Parameters:
        data (:py:obj:`str`):
            The data. Be aware that a bad client can send arbitrary
            data in this field.

        button_text (:py:obj:`str`):
            Text of the web_app keyboard button from which the Web
            App was opened. Be aware that a bad client can send
            arbitrary data in this field.
    """

    def __init__(self, *, data: str, button_text: str, **_kwargs: Any):
        super().__init__()

        self.data = data
        self.button_text = button_text

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["WebAppData"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
