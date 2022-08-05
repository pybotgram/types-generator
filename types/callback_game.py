from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class CallbackGame(Object):
    """A placeholder, currently holds no information. Use BotFather to set up
    your game.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__()

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["CallbackGame"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
