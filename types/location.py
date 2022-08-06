from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class Location(Object):
    """This object represents a point on the map.

    Parameters:
        longitude (:py:obj:`float`):
            Longitude as defined by sender.

        latitude (:py:obj:`float`):
            Latitude as defined by sender.

        horizontal_accuracy (:py:obj:`float`, *optional*):
            The radius of uncertainty for the location, measured in
            meters; 0-1500.

        live_period (:py:obj:`int`, *optional*):
            Time relative to the message sending date, during which
            the location can be updated; in seconds. For active live
            locations only.

        heading (:py:obj:`int`, *optional*):
            The direction in which user is moving, in degrees; 1-360.
            For active live locations only.

        proximity_alert_radius (:py:obj:`int`, *optional*):
            The maximum distance for proximity alerts about
            approaching another chat member, in meters. For sent live
            locations only.
    """

    def __init__(
        self,
        *,
        longitude: float,
        latitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.longitude = longitude
        self.latitude = latitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Location"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
