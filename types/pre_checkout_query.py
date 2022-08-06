from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class PreCheckoutQuery(Object):
    """This object contains information about an incoming pre-checkout query.

    Parameters:
        id (:py:obj:`str`):
            Unique query identifier.

        from_user (:obj:`~pybotgram.types.User`):
            User who sent the query.

        currency (:py:obj:`str`):
            Three-letter ISO 4217 currency code.

        total_amount (:py:obj:`int`):
            Total price in the smallest units of the currency
            (integer, not float/double). For example, for a price of
            US$ 1.45 pass amount = 145. See the exp parameter in
            currencies.json, it shows the number of digits past the
            decimal point for each currency (2 for the majority of
            currencies).

        invoice_payload (:py:obj:`str`):
            Bot specified invoice payload.

        shipping_option_id (:py:obj:`str`, *optional*):
            Identifier of the shipping option chosen by the user.

        order_info (:obj:`~pybotgram.types.OrderInfo`, *optional*):
            Order information provided by the user.
    """

    def __init__(
        self,
        *,
        id: str,
        from_user: "types.User",
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional["types.OrderInfo"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.from_user = from_user
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PreCheckoutQuery"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from_user"] = types.User._parse(data.get("from"), bot)
        data["order_info"] = types.OrderInfo._parse(
            data.get("order_info"), bot
        )

        return cls(bot=bot, **data)
