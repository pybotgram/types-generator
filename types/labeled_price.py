from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class LabeledPrice(Object):
    """This object represents a portion of the price for goods or services.

    Parameters:
        label (``str``):
            Portion label.

        amount (``int``):
            Price of the product in the smallest units of the
            currency (integer, not float/double). For example, for a
            price of US$ 1.45 pass amount = 145. See the exp parameter
            in currencies.json, it shows the number of digits past the
            decimal point for each currency (2 for the majority of
            currencies).
    """

    def __init__(self, *, label: str, amount: int, **_kwargs: Any):
        super().__init__()

        self.label = label
        self.amount = amount

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["LabeledPrice"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
