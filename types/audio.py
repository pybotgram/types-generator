from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class Audio(Object):
    """This object represents an audio file to be treated as music by the
    Telegram clients.

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        duration (:py:obj:`int`):
            Duration of the audio in seconds as defined by sender.

        performer (:py:obj:`str`, *optional*):
            Performer of the audio as defined by sender or by audio
            tags.

        title (:py:obj:`str`, *optional*):
            Title of the audio as defined by sender or by audio tags.

        file_name (:py:obj:`str`, *optional*):
            Original filename as defined by sender.

        mime_type (:py:obj:`str`, *optional*):
            MIME type of the file as defined by sender.

        file_size (:py:obj:`int`, *optional*):
            File size in bytes. It can be bigger than 2^31 and some
            programming languages may have difficulty/silent defects
            in interpreting it. But it has at most 52 significant
            bits, so a signed 64-bit integer or double-precision float
            type are safe for storing this value.

        thumb (:obj:`~pybotgram.types.PhotoSize`, *optional*):
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
