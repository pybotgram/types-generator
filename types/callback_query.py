from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class CallbackQuery(Object):
    """This object represents an incoming callback query from a callback
    button in an inline keyboard. If the button that originated the
    query was attached to a message sent by the bot, the field message
    will be present. If the button was attached to a message sent via
    the bot (in inline mode), the field inline_message_id will be
    present. Exactly one of the fields data or game_short_name will be
    present.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this query.

        from_user (:obj:`~pybotgram.types.User`):
            Sender.

        message (:obj:`~pybotgram.types.Message`, *optional*):
            Message with the callback button that originated the
            query. Note that message content and message date will not
            be available if the message is too old.

        inline_message_id (:py:obj:`str`, *optional*):
            Identifier of the message sent via the bot in inline
            mode, that originated the query.

        chat_instance (:py:obj:`str`):
            Global identifier, uniquely corresponding to the chat to
            which the message with the callback button was sent.
            Useful for high scores in games.

        data (:py:obj:`str`, *optional*):
            Data associated with the callback button. Be aware that
            the message originated the query can contain no callback
            buttons with this data.

        game_short_name (:py:obj:`str`, *optional*):
            Short name of a Game to be returned, serves as the unique
            identifier for the game.
    """

    def __init__(
        self,
        *,
        id: str,
        from_user: "types.User",
        message: Optional["types.Message"] = None,
        inline_message_id: Optional[str] = None,
        chat_instance: str,
        data: Optional[str] = None,
        game_short_name: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.from_user = from_user
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["CallbackQuery"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from_user"] = types.User._parse(data.get("from"), bot)
        data["message"] = types.Message._parse(data.get("message"), bot)

        return cls(bot=bot, **data)
