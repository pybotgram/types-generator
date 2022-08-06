from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class Dice(Object):
    """This object represents an animated emoji that displays a random value.

    Parameters:
        emoji (:py:obj:`str`):
            Emoji on which the dice throw animation is based.

        value (:py:obj:`int`):
            Value of the dice, 1-6 for "", "" and "" base emoji, 1-5
            for "" and "" base emoji, 1-64 for "" base emoji.
    """

    def __init__(self, *, emoji: str, value: int, **_kwargs: Any):
        super().__init__()

        self.emoji = emoji
        self.value = value

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Dice"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
