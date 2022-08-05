from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ChatMemberUpdated(Object):
    """This object represents changes in the status of a chat member.

    Parameters:
        chat (`~pybotgram.types.Chat`):
            Chat the user belongs to.

        from_user (`~pybotgram.types.User`):
            Performer of the action, which resulted in the change.

        date (``int``):
            Date the change was done in Unix time.

        old_chat_member (`~pybotgram.types.ChatMember`):
            Previous information about the chat member.

        new_chat_member (`~pybotgram.types.ChatMember`):
            New information about the chat member.

        invite_link (`~pybotgram.types.ChatInviteLink`, *optional*):
            Chat invite link, which was used by the user to join the
            chat; for joining by invite link events only.
    """

    def __init__(
        self,
        *,
        chat: "types.Chat",
        from_user: "types.User",
        date: int,
        old_chat_member: "types.ChatMember",
        new_chat_member: "types.ChatMember",
        invite_link: Optional["types.ChatInviteLink"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberUpdated"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["chat"] = types.Chat._parse(data.get("chat"), bot)
        data["from"] = types.User._parse(data.get("from"), bot)
        data["old_chat_member"] = types.ChatMember._parse(
            data.get("old_chat_member"), bot
        )
        data["new_chat_member"] = types.ChatMember._parse(
            data.get("new_chat_member"), bot
        )
        data["invite_link"] = types.ChatInviteLink._parse(
            data.get("invite_link"), bot
        )

        return cls(bot=bot, **data)
