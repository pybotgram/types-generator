from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class SentWebAppMessage(Object):
    """Describes an inline message sent by a Web App on behalf of a user.

    Parameters:
        inline_message_id (:py:obj:`str`, *optional*):
            Identifier of the sent inline message. Available only if
            there is an inline keyboard attached to the message.
    """

    def __init__(
        self, *, inline_message_id: Optional[str] = None, **_kwargs: Any
    ):
        super().__init__()

        self.inline_message_id = inline_message_id

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["SentWebAppMessage"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
