from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class KeyboardButtonPollType(Object):
    """This object represents type of a poll, which is allowed to be created
    and sent when the corresponding button is pressed.

    Parameters:
        type (:py:obj:`str`, *optional*):
            If quiz is passed, the user will be allowed to create
            only polls in the quiz mode. If regular is passed, only
            regular polls will be allowed. Otherwise, the user will be
            allowed to create a poll of any type.
    """

    def __init__(self, *, type: Optional[str] = None, **_kwargs: Any):
        super().__init__()

        self.type = type

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["KeyboardButtonPollType"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
