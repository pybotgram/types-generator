from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class PollOption(Object):
    """This object contains information about one answer option in a poll.

    Parameters:
        text (:obj:`str`):
            Option text, 1-100 characters.

        voter_count (:obj:`int`):
            Number of users that voted for this option.
    """

    def __init__(self, *, text: str, voter_count: int, **_kwargs: Any):
        super().__init__()

        self.text = text
        self.voter_count = voter_count

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PollOption"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
