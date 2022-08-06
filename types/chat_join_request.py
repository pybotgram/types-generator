from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class ChatJoinRequest(Object):
    """Represents a join request sent to a chat.

    Parameters:
        chat (:obj:`~pybotgram.types.Chat`):
            Chat to which the request was sent.

        from_user (:obj:`~pybotgram.types.User`):
            User that sent the join request.

        date (:py:obj:`int`):
            Date the request was sent in Unix time.

        bio (:py:obj:`str`, *optional*):
            Bio of the user.

        invite_link (:obj:`~pybotgram.types.ChatInviteLink`, *optional*):
            Chat invite link that was used by the user to send the
            join request.
    """

    def __init__(
        self,
        *,
        chat: "types.Chat",
        from_user: "types.User",
        date: int,
        bio: Optional[str] = None,
        invite_link: Optional["types.ChatInviteLink"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.bio = bio
        self.invite_link = invite_link

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatJoinRequest"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["chat"] = types.Chat._parse(data.get("chat"), bot)
        data["from_user"] = types.User._parse(data.get("from"), bot)
        data["invite_link"] = types.ChatInviteLink._parse(
            data.get("invite_link"), bot
        )

        return cls(bot=bot, **data)
