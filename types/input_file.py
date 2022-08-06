from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class InputFile(Object):
    """This object represents the contents of a file to be uploaded. Must be
    posted using multipart/form-data in the usual way that files are
    uploaded via the browser.
    """

    def __init__(self, **_kwargs: Any):
        super().__init__()

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["InputFile"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
