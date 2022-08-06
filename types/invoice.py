from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class Invoice(Object):
    """This object contains basic information about an invoice.

    Parameters:
        title (:py:obj:`str`):
            Product name.

        description (:py:obj:`str`):
            Product description.

        start_parameter (:py:obj:`str`):
            Unique bot deep-linking parameter that can be used to
            generate this invoice.

        currency (:py:obj:`str`):
            Three-letter ISO 4217 currency code.

        total_amount (:py:obj:`int`):
            Total price in the smallest units of the currency
            (integer, not float/double). For example, for a price of
            US$ 1.45 pass amount = 145. See the exp parameter in
            currencies.json, it shows the number of digits past the
            decimal point for each currency (2 for the majority of
            currencies).
    """

    def __init__(
        self,
        *,
        title: str,
        description: str,
        start_parameter: str,
        currency: str,
        total_amount: int,
        **_kwargs: Any
    ):
        super().__init__()

        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Invoice"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
