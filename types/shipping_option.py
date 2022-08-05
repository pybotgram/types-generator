from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ShippingOption(Object):
    """This object represents one shipping option.

    Parameters:
        id (``str``):
            Shipping option identifier.

        title (``str``):
            Option title.

        prices (List of `~pybotgram.types.LabeledPrice`):
            List of price portions.
    """

    def __init__(
        self,
        *,
        id: str,
        title: str,
        prices: List["types.LabeledPrice"],
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.title = title
        self.prices = prices

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ShippingOption"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["prices"] = types.LabeledPrice._parse_list(
            data.get("prices"), bot
        )

        return cls(bot=bot, **data)
