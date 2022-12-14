from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class Animation(Object):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC
    video without sound).

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        width (:py:obj:`int`):
            Video width as defined by sender.

        height (:py:obj:`int`):
            Video height as defined by sender.

        duration (:py:obj:`int`):
            Duration of the video in seconds as defined by sender.

        thumb (:obj:`~pybotgram.types.PhotoSize`, *optional*):
            Animation thumbnail as defined by sender.

        file_name (:py:obj:`str`, *optional*):
            Original animation filename as defined by sender.

        mime_type (:py:obj:`str`, *optional*):
            MIME type of the file as defined by sender.

        file_size (:py:obj:`int`, *optional*):
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
    ) -> Optional["Animation"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)

        return cls(bot=bot, **data)
