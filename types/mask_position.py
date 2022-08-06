from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class MaskPosition(Object):
    """This object describes the position on faces where a mask should be
    placed by default.

    Parameters:
        point (:py:obj:`str`):
            The part of the face relative to which the mask should be
            placed. One of "forehead", "eyes", "mouth", or "chin".

        x_shift (:py:obj:`float`):
            Shift by X-axis measured in widths of the mask scaled to
            the face size, from left to right. For example, choosing
            -1.0 will place mask just to the left of the default mask
            position.

        y_shift (:py:obj:`float`):
            Shift by Y-axis measured in heights of the mask scaled to
            the face size, from top to bottom. For example, 1.0 will
            place the mask just below the default mask position.

        scale (:py:obj:`float`):
            Mask scaling coefficient. For example, 2.0 means double
            size.
    """

    def __init__(
        self,
        *,
        point: str,
        x_shift: float,
        y_shift: float,
        scale: float,
        **_kwargs: Any
    ):
        super().__init__()

        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["MaskPosition"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
