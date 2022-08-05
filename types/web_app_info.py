from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class WebAppInfo(Object):
    """Describes a Web App.

    Parameters:
        url (``str``):
            An HTTPS URL of a Web App to be opened with additional
            data as specified in Initializing Web Apps.
    """

    def __init__(self, *, url: str, **_kwargs: Any):
        super().__init__()

        self.url = url

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["WebAppInfo"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
