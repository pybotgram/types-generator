from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class InlineKeyboardMarkup(Object):
    """This object represents an inline keyboard that appears right next to
    the message it belongs to.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will display unsupported message.

    Parameters:
        inline_keyboard (List of List of :obj:`~pybotgram.types.InlineKeyboardButton`):
            Array of button rows, each represented by an Array of
            InlineKeyboardButton objects.
    """

    def __init__(
        self,
        *,
        inline_keyboard: List[List["types.InlineKeyboardButton"]],
        **_kwargs: Any
    ):
        super().__init__()

        self.inline_keyboard = inline_keyboard

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["InlineKeyboardMarkup"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["inline_keyboard"] = types.InlineKeyboardButton._parse_list(
            data.get("inline_keyboard"), bot
        )

        return cls(bot=bot, **data)
