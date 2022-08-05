from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class PassportFile(Object):
    """This object represents a file uploaded to Telegram Passport. Currently
    all Telegram Passport files are in JPEG format when decrypted and
    don't exceed 10MB.

    Parameters:
        file_id (``str``):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (``str``):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        file_size (``int``):
            File size in bytes.

        file_date (``int``):
            Unix time when the file was uploaded.
    """

    def __init__(
        self,
        *,
        file_id: str,
        file_unique_id: str,
        file_size: int,
        file_date: int,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.file_size = file_size
        self.file_date = file_date

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PassportFile"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
