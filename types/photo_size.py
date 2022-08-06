from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class PhotoSize(Object):
    """This object represents one size of a photo or a file / sticker
    thumbnail.

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        width (:py:obj:`int`):
            Photo width.

        height (:py:obj:`int`):
            Photo height.

        file_size (:py:obj:`int`, *optional*):
            File size in bytes.
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        width: int,
        height: int,
        file_size: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PhotoSize"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
