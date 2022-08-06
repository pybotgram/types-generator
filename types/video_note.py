from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class VideoNote(Object):
    """This object represents a video message (available in Telegram apps as
    of v.4.0).

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        length (:py:obj:`int`):
            Video width and height (diameter of the video message) as
            defined by sender.

        duration (:py:obj:`int`):
            Duration of the video in seconds as defined by sender.

        thumb (:obj:`~pybotgram.types.PhotoSize`, *optional*):
            Video thumbnail.

        file_size (:py:obj:`int`, *optional*):
            File size in bytes.
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        length: int,
        duration: int,
        thumb: Optional["types.PhotoSize"] = None,
        file_size: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumb = thumb
        self.file_size = file_size

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["VideoNote"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)

        return cls(bot=bot, **data)
