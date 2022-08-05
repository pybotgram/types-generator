from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class InlineQuery(Object):
    """This object represents an incoming inline query. When the user sends
    an empty query, your bot could return some default or trending
    results.

    Parameters:
        id (:obj:`str`):
            Unique identifier for this query.

        from_user (:obj:`~pybotgram.types.User`):
            Sender.

        query (:obj:`str`):
            Text of the query (up to 256 characters).

        offset (:obj:`str`):
            Offset of the results to be returned, can be controlled
            by the bot.

        chat_type (:obj:`str`, *optional*):
            Type of the chat from which the inline query was sent.
            Can be either "sender" for a private chat with the inline
            query sender, "private", "group", "supergroup", or
            "channel". The chat type should be always known for
            requests sent from official clients and most third-party
            clients, unless the request was sent from a secret chat.

        location (:obj:`~pybotgram.types.Location`, *optional*):
            Sender location, only for bots that request user location.
    """

    def __init__(
        self,
        *,
        id: str,
        from_user: "types.User",
        query: str,
        offset: str,
        chat_type: Optional[str] = None,
        location: Optional["types.Location"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.from_user = from_user
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["InlineQuery"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from"] = types.User._parse(data.get("from"), bot)
        data["location"] = types.Location._parse(data.get("location"), bot)

        return cls(bot=bot, **data)
