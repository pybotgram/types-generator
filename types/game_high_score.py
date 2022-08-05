from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class GameHighScore(Object):
    """This object represents one row of the high scores table for a game.

    Parameters:
        position (``int``):
            Position in high score table for the game.

        user (`~pybotgram.types.User`):
            User.

        score (``int``):
            Score.
    """

    def __init__(
        self, *, position: int, user: "types.User", score: int, **_kwargs: Any
    ):
        super().__init__()

        self.position = position
        self.user = user
        self.score = score

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["GameHighScore"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)
