from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class VideoChatStarted(Object):
    """This object represents a service message about a video chat started in
    the chat. Currently holds no information.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__()

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["VideoChatStarted"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
