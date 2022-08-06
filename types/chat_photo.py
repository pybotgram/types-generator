from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class ChatPhoto(Object):
    """This object represents a chat photo.

    Parameters:
        small_file_id (:py:obj:`str`):
            File identifier of small (160x160) chat photo. This
            file_id can be used only for photo download and only for
            as long as the photo is not changed.

        small_file_unique_id (:py:obj:`str`):
            Unique file identifier of small (160x160) chat photo,
            which is supposed to be the same over time and for
            different bots. Can't be used to download or reuse the
            file.

        big_file_id (:py:obj:`str`):
            File identifier of big (640x640) chat photo. This file_id
            can be used only for photo download and only for as long
            as the photo is not changed.

        big_file_unique_id (:py:obj:`str`):
            Unique file identifier of big (640x640) chat photo, which
            is supposed to be the same over time and for different
            bots. Can't be used to download or reuse the file.
    """

    def __init__(
        self,
        *,
        small_file_id: str,
        small_file_unique_id: str,
        big_file_id: str,
        big_file_unique_id: str,
        **_kwargs: Any
    ):
        super().__init__()

        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ChatPhoto"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
