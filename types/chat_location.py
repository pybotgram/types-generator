from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ChatLocation(Object):
    """Represents a location to which a chat is connected.

    Parameters:
        location (:obj:`~pybotgram.types.Location`):
            The location to which the supergroup is connected. Can't
            be a live location.

        address (:py:obj:`str`):
            Location address; 1-64 characters, as defined by the chat
            owner.
    """

    def __init__(
        self, *, location: "types.Location", address: str, **_kwargs: Any
    ):
        super().__init__()

        self.location = location
        self.address = address

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatLocation"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["location"] = types.Location._parse(data.get("location"), bot)

        return cls(bot=bot, **data)
