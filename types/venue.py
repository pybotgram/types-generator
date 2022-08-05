from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Venue(Object):
    """This object represents a venue.

    Parameters:
        location (:obj:`~pybotgram.types.Location`):
            Venue location. Can't be a live location.

        title (:obj:`str`):
            Name of the venue.

        address (:obj:`str`):
            Address of the venue.

        foursquare_id (:obj:`str`, *optional*):
            Foursquare identifier of the venue.

        foursquare_type (:obj:`str`, *optional*):
            Foursquare type of the venue. (For example,
            "arts_entertainment/default",
            "arts_entertainment/aquarium" or "food/icecream".).

        google_place_id (:obj:`str`, *optional*):
            Google Places identifier of the venue.

        google_place_type (:obj:`str`, *optional*):
            Google Places type of the venue. (See supported types.).
    """

    def __init__(
        self,
        *,
        location: "types.Location",
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Venue"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["location"] = types.Location._parse(data.get("location"), bot)

        return cls(bot=bot, **data)
