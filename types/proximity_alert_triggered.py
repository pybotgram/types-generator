from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class ProximityAlertTriggered(Object):
    """This object represents the content of a service message, sent whenever
    a user in the chat triggers a proximity alert set by another user.

    Parameters:
        traveler (:obj:`~pybotgram.types.User`):
            User that triggered the alert.

        watcher (:obj:`~pybotgram.types.User`):
            User that set the alert.

        distance (:py:obj:`int`):
            The distance between the users.
    """

    def __init__(
        self,
        *,
        traveler: "types.User",
        watcher: "types.User",
        distance: int,
        **_kwargs: Any
    ):
        super().__init__()

        self.traveler = traveler
        self.watcher = watcher
        self.distance = distance

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ProximityAlertTriggered"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["traveler"] = types.User._parse(data.get("traveler"), bot)
        data["watcher"] = types.User._parse(data.get("watcher"), bot)

        return cls(bot=bot, **data)
