from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class VideoChatParticipantsInvited(Object):
    """This object represents a service message about new members invited to
    a video chat.

    Parameters:
        users (List of :obj:`~pybotgram.types.User`):
            New members that were invited to the video chat.
    """

    def __init__(self, *, users: List["types.User"], **_kwargs: Any):
        super().__init__()

        self.users = users

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["VideoChatParticipantsInvited"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["users"] = types.User._parse_list(data.get("users"), bot)

        return cls(bot=bot, **data)
