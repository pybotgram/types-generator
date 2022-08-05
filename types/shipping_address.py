from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class ShippingAddress(Object):
    """This object represents a shipping address.

    Parameters:
        country_code (:obj:`str`):
            Two-letter ISO 3166-1 alpha-2 country code.

        state (:obj:`str`):
            State, if applicable.

        city (:obj:`str`):
            City.

        street_line1 (:obj:`str`):
            First line for the address.

        street_line2 (:obj:`str`):
            Second line for the address.

        post_code (:obj:`str`):
            Address post code.
    """

    def __init__(
        self,
        *,
        country_code: str,
        state: str,
        city: str,
        street_line1: str,
        street_line2: str,
        post_code: str,
        **_kwargs: Any
    ):
        super().__init__()

        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ShippingAddress"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
