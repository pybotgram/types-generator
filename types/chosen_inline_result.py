from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ChosenInlineResult(Object):
    """Represents a result of an inline query that was chosen by the user and
    sent to their chat partner.
    Note: It is necessary to enable inline feedback via @BotFather in
    order to receive these objects in updates.

    Parameters:
        result_id (:py:obj:`str`):
            The unique identifier for the result that was chosen.

        from_user (:obj:`~pybotgram.types.User`):
            The user that chose the result.

        location (:obj:`~pybotgram.types.Location`, *optional*):
            Sender location, only for bots that require user location.

        inline_message_id (:py:obj:`str`, *optional*):
            Identifier of the sent inline message. Available only if
            there is an inline keyboard attached to the message. Will
            be also received in callback queries and can be used to
            edit the message.

        query (:py:obj:`str`):
            The query that was used to obtain the result.
    """

    def __init__(
        self,
        *,
        result_id: str,
        from_user: "types.User",
        location: Optional["types.Location"] = None,
        inline_message_id: Optional[str] = None,
        query: str,
        **_kwargs: Any
    ):
        super().__init__()

        self.result_id = result_id
        self.from_user = from_user
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChosenInlineResult"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from_user"] = types.User._parse(data.get("from"), bot)
        data["location"] = types.Location._parse(data.get("location"), bot)

        return cls(bot=bot, **data)
