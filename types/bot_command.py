from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class BotCommand(Object):
    """This object represents a bot command.

    Parameters:
        command (:py:obj:`str`):
            Text of the command; 1-32 characters. Can contain only
            lowercase English letters, digits and underscores.

        description (:py:obj:`str`):
            Description of the command; 1-256 characters.
    """

    def __init__(self, *, command: str, description: str, **_kwargs: Any):
        super().__init__()

        self.command = command
        self.description = description

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["BotCommand"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
