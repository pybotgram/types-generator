from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class ChatPermissions(Object):
    """Describes actions that a non-administrator user is allowed to take in
    a chat.

    Parameters:
        can_send_messages (:py:obj:`bool`, *optional*):
            True, if the user is allowed to send text messages,
            contacts, locations and venues.

        can_send_media_messages (:py:obj:`bool`, *optional*):
            True, if the user is allowed to send audios, documents,
            photos, videos, video notes and voice notes, implies
            can_send_messages.

        can_send_polls (:py:obj:`bool`, *optional*):
            True, if the user is allowed to send polls, implies
            can_send_messages.

        can_send_other_messages (:py:obj:`bool`, *optional*):
            True, if the user is allowed to send animations, games,
            stickers and use inline bots, implies
            can_send_media_messages.

        can_add_web_page_previews (:py:obj:`bool`, *optional*):
            True, if the user is allowed to add web page previews to
            their messages, implies can_send_media_messages.

        can_change_info (:py:obj:`bool`, *optional*):
            True, if the user is allowed to change the chat title,
            photo and other settings. Ignored in public supergroups.

        can_invite_users (:py:obj:`bool`, *optional*):
            True, if the user is allowed to invite new users to the
            chat.

        can_pin_messages (:py:obj:`bool`, *optional*):
            True, if the user is allowed to pin messages. Ignored in
            public supergroups.
    """

    def __init__(
        self,
        *,
        can_send_messages: Optional[bool] = None,
        can_send_media_messages: Optional[bool] = None,
        can_send_polls: Optional[bool] = None,
        can_send_other_messages: Optional[bool] = None,
        can_add_web_page_previews: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatPermissions"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
