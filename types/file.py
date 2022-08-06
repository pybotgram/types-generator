from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class File(Object):
    """This object represents a file ready to be downloaded. The file can be
    downloaded via the link
    https://api.telegram.org/file/bot<token>/<file_path>. It is
    guaranteed that the link will be valid for at least 1 hour. When
    the link expires, a new one can be requested by calling getFile.

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        file_size (:py:obj:`int`, *optional*):
            File size in bytes. It can be bigger than 2^31 and some
            programming languages may have difficulty/silent defects
            in interpreting it. But it has at most 52 significant
            bits, so a signed 64-bit integer or double-precision float
            type are safe for storing this value.

        file_path (:py:obj:`str`, *optional*):
            File path. Use
            https://api.telegram.org/file/bot<token>/<file_path> to
            get the file.
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        file_size: Optional[int] = None,
        file_path: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_path = file_path

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["File"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
