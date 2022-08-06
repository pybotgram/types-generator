from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class Contact(Object):
    """This object represents a phone contact.

    Parameters:
        phone_number (:py:obj:`str`):
            Contact's phone number.

        first_name (:py:obj:`str`):
            Contact's first name.

        last_name (:py:obj:`str`, *optional*):
            Contact's last name.

        user_id (:py:obj:`int`, *optional*):
            Contact's user identifier in Telegram. This number may
            have more than 32 significant bits and some programming
            languages may have difficulty/silent defects in
            interpreting it. But it has at most 52 significant bits,
            so a 64-bit integer or double-precision float type are
            safe for storing this identifier.

        vcard (:py:obj:`str`, *optional*):
            Additional data about the contact in the form of a vCard.
    """

    def __init__(
        self,
        *,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        user_id: Optional[int] = None,
        vcard: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Contact"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
