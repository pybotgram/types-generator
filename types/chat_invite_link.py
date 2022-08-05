from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ChatInviteLink(Object):
    """Represents an invite link for a chat.

    Parameters:
        invite_link (``str``):
            The invite link. If the link was created by another chat
            administrator, then the second part of the link will be
            replaced with "…".

        creator (`~pybotgram.types.User`):
            Creator of the link.

        creates_join_request (``bool``):
            True, if users joining the chat via the link need to be
            approved by chat administrators.

        is_primary (``bool``):
            True, if the link is primary.

        is_revoked (``bool``):
            True, if the link is revoked.

        name (``str``, *optional*):
            Invite link name.

        expire_date (``int``, *optional*):
            Point in time (Unix timestamp) when the link will expire
            or has been expired.

        member_limit (``int``, *optional*):
            The maximum number of users that can be members of the
            chat simultaneously after joining the chat via this invite
            link; 1-99999.

        pending_join_request_count (``int``, *optional*):
            Number of pending join requests created using this link.
    """

    def __init__(
        self,
        *,
        invite_link: str,
        creator: "types.User",
        creates_join_request: bool,
        is_primary: bool,
        is_revoked: bool,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        pending_join_request_count: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.invite_link = invite_link
        self.creator = creator
        self.creates_join_request = creates_join_request
        self.is_primary = is_primary
        self.is_revoked = is_revoked
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.pending_join_request_count = pending_join_request_count

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatInviteLink"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["creator"] = types.User._parse(data.get("creator"), bot)

        return cls(bot=bot, **data)
