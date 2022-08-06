from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class MessageId(Object):
    """This object represents a unique message identifier.

    Parameters:
        message_id (:py:obj:`int`):
            Unique message identifier.
    """

    def __init__(self, *, message_id: int, **_kwargs: Any):
        super().__init__()

        self.message_id = message_id

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["MessageId"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
