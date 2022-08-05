from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class VideoChatScheduled(Object):
    """This object represents a service message about a video chat scheduled
    in the chat.

    Parameters:
        start_date (:obj:`int`):
            Point in time (Unix timestamp) when the video chat is
            supposed to be started by a chat administrator.
    """

    def __init__(self, *, start_date: int, **_kwargs: Any):
        super().__init__()

        self.start_date = start_date

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["VideoChatScheduled"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
