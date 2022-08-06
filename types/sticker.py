from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class Sticker(Object):
    """This object represents a sticker.

    Parameters:
        file_id (:py:obj:`str`):
            Identifier for this file, which can be used to download
            or reuse the file.

        file_unique_id (:py:obj:`str`):
            Unique identifier for this file, which is supposed to be
            the same over time and for different bots. Can't be used
            to download or reuse the file.

        width (:py:obj:`int`):
            Sticker width.

        height (:py:obj:`int`):
            Sticker height.

        is_animated (:py:obj:`bool`):
            True, if the sticker is animated.

        is_video (:py:obj:`bool`):
            True, if the sticker is a video sticker.

        thumb (:obj:`~pybotgram.types.PhotoSize`, *optional*):
            Sticker thumbnail in the .WEBP or .JPG format.

        emoji (:py:obj:`str`, *optional*):
            Emoji associated with the sticker.

        set_name (:py:obj:`str`, *optional*):
            Name of the sticker set to which the sticker belongs.

        premium_animation (:obj:`~pybotgram.types.File`, *optional*):
            Premium animation for the sticker, if the sticker is
            premium.

        mask_position (:obj:`~pybotgram.types.MaskPosition`, *optional*):
            For mask stickers, the position where the mask should be
            placed.

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
        is_animated: bool,
        is_video: bool,
        thumb: Optional["types.PhotoSize"] = None,
        emoji: Optional[str] = None,
        set_name: Optional[str] = None,
        premium_animation: Optional["types.File"] = None,
        mask_position: Optional["types.MaskPosition"] = None,
        file_size: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumb = thumb
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.file_size = file_size

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Sticker"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["thumb"] = types.PhotoSize._parse(data.get("thumb"), bot)
        data["premium_animation"] = types.File._parse(
            data.get("premium_animation"), bot
        )
        data["mask_position"] = types.MaskPosition._parse(
            data.get("mask_position"), bot
        )

        return cls(bot=bot, **data)
