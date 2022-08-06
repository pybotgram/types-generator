from typing import Optional, List, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class UserProfilePhotos(Object):
    """This object represent a user's profile pictures.

    Parameters:
        total_count (:py:obj:`int`):
            Total number of profile pictures the target user has.

        photos (List of List of :obj:`~pybotgram.types.PhotoSize`):
            Requested profile pictures (in up to 4 sizes each).
    """

    def __init__(
        self,
        *,
        total_count: int,
        photos: List[List["types.PhotoSize"]],
        **_kwargs: Any
    ):
        super().__init__()

        self.total_count = total_count
        self.photos = photos

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["UserProfilePhotos"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["photos"] = types.PhotoSize._parse_list(data.get("photos"), bot)

        return cls(bot=bot, **data)
