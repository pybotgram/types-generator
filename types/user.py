from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class User(Object):
    """This object represents a Telegram user or bot.

    Parameters:
        id (:py:obj:`int`):
            Unique identifier for this user or bot. This number may
            have more than 32 significant bits and some programming
            languages may have difficulty/silent defects in
            interpreting it. But it has at most 52 significant bits,
            so a 64-bit integer or double-precision float type are
            safe for storing this identifier.

        is_bot (:py:obj:`bool`):
            True, if this user is a bot.

        first_name (:py:obj:`str`):
            User's or bot's first name.

        last_name (:py:obj:`str`, *optional*):
            User's or bot's last name.

        username (:py:obj:`str`, *optional*):
            User's or bot's username.

        language_code (:py:obj:`str`, *optional*):
            IETF language tag of the user's language.

        is_premium (:py:obj:`bool`, *optional*):
            True, if this user is a Telegram Premium user.

        added_to_attachment_menu (:py:obj:`bool`, *optional*):
            True, if this user added the bot to the attachment menu.

        can_join_groups (:py:obj:`bool`, *optional*):
            True, if the bot can be invited to groups. Returned only
            in getMe.

        can_read_all_group_messages (:py:obj:`bool`, *optional*):
            True, if privacy mode is disabled for the bot. Returned
            only in getMe.

        supports_inline_queries (:py:obj:`bool`, *optional*):
            True, if the bot supports inline queries. Returned only
            in getMe.
    """

    def __init__(
        self,
        *,
        id: int,
        is_bot: bool,
        first_name: str,
        last_name: Optional[str] = None,
        username: Optional[str] = None,
        language_code: Optional[str] = None,
        is_premium: Optional[bool] = None,
        added_to_attachment_menu: Optional[bool] = None,
        can_join_groups: Optional[bool] = None,
        can_read_all_group_messages: Optional[bool] = None,
        supports_inline_queries: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["User"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
