from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Video(Object):
    """This object represents a video file.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        width (``int``):
            Video width as defined by sender.

        height (``int``):
            Video height as defined by sender.

        duration (``int``):
            Duration of the video in seconds as defined by sender.

        thumb (`~pybotgram.types.PhotoSize`, *optional*):
            Video thumbnail.

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
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        duration: int,
        thumb: Optional["types.PhotoSize"] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        file_size: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Video"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)

        return cls(bot=bot, **data)
