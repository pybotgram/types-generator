from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class VideoChatEnded(Object):
    """This object represents a service message about a video chat ended in
    the chat.

    Parameters:
        duration (:obj:`int`):
            Video chat duration in seconds.
    """

    def __init__(self, *, duration: int, **_kwargs: Any):
        super().__init__()

        self.duration = duration

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["VideoChatEnded"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
