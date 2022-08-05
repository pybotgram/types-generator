from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class StickerSet(Object):
    """This object represents a sticker set.

    Parameters:
        name (``str``):
            Sticker set name.

        title (``str``):
            Sticker set title.

        is_animated (``bool``):
            True, if the sticker set contains animated stickers.

        is_video (``bool``):
            True, if the sticker set contains video stickers.

        contains_masks (``bool``):
            True, if the sticker set contains masks.

        stickers (List of `~pybotgram.types.Sticker`):
            List of all set stickers.

        thumb (`~pybotgram.types.PhotoSize`, *optional*):
            Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format.
    """

    def __init__(
        self,
        *,
        name: str,
        title: str,
        is_animated: bool,
        is_video: bool,
        contains_masks: bool,
        stickers: List["types.Sticker"],
        thumb: Optional["types.PhotoSize"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.name = name
        self.title = title
        self.is_animated = is_animated
        self.is_video = is_video
        self.contains_masks = contains_masks
        self.stickers = stickers
        self.thumb = thumb

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["StickerSet"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["stickers"] = types.Sticker._parse_list(data.get("stickers"), bot)
        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)

        return cls(bot=bot, **data)
