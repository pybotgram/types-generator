from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class MessageEntity(Object):
    """This object represents one special entity in a text message. For
    example, hashtags, usernames, URLs, etc.

    Parameters:
        type (:obj:`str`):
            Type of the entity. Currently, can be "mention"
            (@username), "hashtag" (#hashtag), "cashtag" ($USD),
            "bot_command" (/start@jobs_bot), "url"
            (https://telegram.org), "email" (do-not-
            reply@telegram.org), "phone_number" (+1-212-555-0123),
            "bold" (bold text), "italic" (italic text), "underline"
            (underlined text), "strikethrough" (strikethrough text),
            "spoiler" (spoiler message), "code" (monowidth string),
            "pre" (monowidth block), "text_link" (for clickable text
            URLs), "text_mention" (for users without usernames).

        offset (:obj:`int`):
            Offset in UTF-16 code units to the start of the entity.

        length (:obj:`int`):
            Length of the entity in UTF-16 code units.

        url (:obj:`str`, *optional*):
            For "text_link" only, URL that will be opened after user
            taps on the text.

        user (:obj:`~pybotgram.types.User`, *optional*):
            For "text_mention" only, the mentioned user.

        language (:obj:`str`, *optional*):
            For "pre" only, the programming language of the entity
            text.
    """

    def __init__(
        self,
        *,
        type: str,
        offset: int,
        length: int,
        url: Optional[str] = None,
        user: Optional["types.User"] = None,
        language: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.type = type
        self.offset = offset
        self.length = length
        self.url = url
        self.user = user
        self.language = language

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["MessageEntity"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)
