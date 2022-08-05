from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Game(Object):
    """This object represents a game. Use BotFather to create and edit games,
    their short names will act as unique identifiers.

    Parameters:
        title (``str``):
            Title of the game.

        description (``str``):
            Description of the game.

        photo (List of `~pybotgram.types.PhotoSize`):
            Photo that will be displayed in the game message in
            chats.

        text (``str``, *optional*):
            Brief description of the game or high scores included in
            the game message. Can be automatically edited to include
            current high scores for the game when the bot calls
            setGameScore, or manually edited using editMessageText.
            0-4096 characters.

        text_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            Special entities that appear in text, such as usernames,
            URLs, bot commands, etc.

        animation (`~pybotgram.types.Animation`, *optional*):
            Animation that will be displayed in the game message in
            chats. Upload via BotFather.
    """

    def __init__(
        self,
        *,
        title: str,
        description: str,
        photo: List["types.PhotoSize"],
        text: Optional[str] = None,
        text_entities: Optional[List["types.MessageEntity"]] = None,
        animation: Optional["types.Animation"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Game"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["photo"] = types.PhotoSize._parse_list(data.get("photo"), bot)
        data["text_entities"] = types.MessageEntity._parse_list(
            data.get("text_entities"), bot
        )
        data["animation"] = types.Animation._parse(data.get("animation"), bot)

        return cls(bot=bot, **data)
