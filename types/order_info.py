from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class OrderInfo(Object):
    """This object represents information about an order.

    Parameters:
        name (``str``, *optional*):
            User name.

        phone_number (``str``, *optional*):
            User's phone number.

        email (``str``, *optional*):
            User email.

        shipping_address (`~pybotgram.types.ShippingAddress`, *optional*):
            User shipping address.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        shipping_address: Optional["types.ShippingAddress"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["OrderInfo"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["shipping_address"] = types.ShippingAddress._parse(
            data.get("shipping_address"), bot
        )

        return cls(bot=bot, **data)
