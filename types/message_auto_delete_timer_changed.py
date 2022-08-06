from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class MessageAutoDeleteTimerChanged(Object):
    """This object represents a service message about a change in auto-delete
    timer settings.

    Parameters:
        message_auto_delete_time (:py:obj:`int`):
            New auto-delete time for messages in the chat; in seconds.
    """

    def __init__(self, *, message_auto_delete_time: int, **_kwargs: Any):
        super().__init__()

        self.message_auto_delete_time = message_auto_delete_time

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["MessageAutoDeleteTimerChanged"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
