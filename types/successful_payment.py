from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class SuccessfulPayment(Object):
    """This object contains basic information about a successful payment.

    Parameters:
        currency (:obj:`str`):
            Three-letter ISO 4217 currency code.

        total_amount (:obj:`int`):
            Total price in the smallest units of the currency
            (integer, not float/double). For example, for a price of
            US$ 1.45 pass amount = 145. See the exp parameter in
            currencies.json, it shows the number of digits past the
            decimal point for each currency (2 for the majority of
            currencies).

        invoice_payload (:obj:`str`):
            Bot specified invoice payload.

        shipping_option_id (:obj:`str`, *optional*):
            Identifier of the shipping option chosen by the user.

        order_info (:obj:`~pybotgram.types.OrderInfo`, *optional*):
            Order information provided by the user.

        telegram_payment_charge_id (:obj:`str`):
            Telegram payment identifier.

        provider_payment_charge_id (:obj:`str`):
            Provider payment identifier.
    """

    def __init__(
        self,
        *,
        currency: str,
        total_amount: int,
        invoice_payload: str,
        shipping_option_id: Optional[str] = None,
        order_info: Optional["types.OrderInfo"] = None,
        telegram_payment_charge_id: str,
        provider_payment_charge_id: str,
        **_kwargs: Any
    ):
        super().__init__()

        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["SuccessfulPayment"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["order_info"] = types.OrderInfo._parse(
            data.get("order_info"), bot
        )

        return cls(bot=bot, **data)
