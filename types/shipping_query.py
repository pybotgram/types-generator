from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ShippingQuery(Object):
    """This object contains information about an incoming shipping query.

    Parameters:
        id (:py:obj:`str`):
            Unique query identifier.

        from_user (:obj:`~pybotgram.types.User`):
            User who sent the query.

        invoice_payload (:py:obj:`str`):
            Bot specified invoice payload.

        shipping_address (:obj:`~pybotgram.types.ShippingAddress`):
            User specified shipping address.
    """

    def __init__(
        self,
        *,
        id: str,
        from_user: "types.User",
        invoice_payload: str,
        shipping_address: "types.ShippingAddress",
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.from_user = from_user
        self.invoice_payload = invoice_payload
        self.shipping_address = shipping_address

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ShippingQuery"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from"] = types.User._parse(data.get("from"), bot)
        data["shipping_address"] = types.ShippingAddress._parse(
            data.get("shipping_address"), bot
        )

        return cls(bot=bot, **data)
