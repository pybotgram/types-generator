from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Audio(Object):
    """This object represents an audio file to be treated as music by the
    Telegram clients.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        duration (``int``):
            Duration of the audio in seconds as defined by sender.

        performer (``str``, *optional*):
            Performer of the audio as defined by sender or by audio
            tags.

        title (``str``, *optional*):
            Title of the audio as defined by sender or by audio tags.

        file_name (``str``, *optional*):
            Original filename as defined by sender.

        mime_type (``str``, *optional*):
            MIME type of the file as defined by sender.

        file_size (``int``, *optional*):
            File size in bytes. It can be bigger than 2^31 and some
            programming languages may have difficulty/silent defects
            in interpreting it. But it has at most 52 significant
            bits, so a signed 64-bit integer or double-precision float
            type are safe for storing this value.

        thumb (`~pybotgram.types.PhotoSize`, *optional*):
            Thumbnail of the album cover to which the music file
            belongs.
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        duration: int,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        thumb: Optional["types.PhotoSize"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumb = thumb

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Audio"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)

        return cls(bot=bot, **data)
