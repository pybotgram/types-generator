from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class ForceReply(Object):
    """Upon receiving a message with this object, Telegram clients will
    display a reply interface to the user (act as if the user has
    selected the bot's message and tapped 'Reply'). This can be
    extremely useful if you want to create user-friendly step-by-step
    interfaces without having to sacrifice privacy mode.

    Parameters:
        force_reply (:py:obj:`bool`):
            Shows reply interface to the user, as if they manually
            selected the bot's message and tapped 'Reply'.

        input_field_placeholder (:py:obj:`str`, *optional*):
            The placeholder to be shown in the input field when the
            reply is active; 1-64 characters.

        selective (:py:obj:`bool`, *optional*):
            Use this parameter if you want to force reply from
            specific users only. Targets: 1) users that are @mentioned
            in the text of the Message object; 2) if the bot's message
            is a reply (has reply_to_message_id), sender of the
            original message.
    """

    def __init__(
        self,
        *,
        force_reply: bool,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ForceReply"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
