from typing import Optional, Dict, List, Any

import pybotgram
from .object import Object
from pybotgram import types


class PollAnswer(Object):
    """This object represents an answer of a user in a non-anonymous poll.

    Parameters:
        poll_id (:py:obj:`str`):
            Unique poll identifier.

        user (:obj:`~pybotgram.types.User`):
            The user, who changed the answer to the poll.

        option_ids (List of :py:obj:`int`):
            0-based identifiers of answer options, chosen by the
            user. May be empty if the user retracted their vote.
    """

    def __init__(
        self,
        *,
        poll_id: str,
        user: "types.User",
        option_ids: List[int],
        **_kwargs: Any
    ):
        super().__init__()

        self.poll_id = poll_id
        self.user = user
        self.option_ids = option_ids

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PollAnswer"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)
