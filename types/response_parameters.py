from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class ResponseParameters(Object):
    """Describes why a request was unsuccessful.

    Parameters:
        migrate_to_chat_id (:py:obj:`int`, *optional*):
            The group has been migrated to a supergroup with the
            specified identifier. This number may have more than 32
            significant bits and some programming languages may have
            difficulty/silent defects in interpreting it. But it has
            at most 52 significant bits, so a signed 64-bit integer or
            double-precision float type are safe for storing this
            identifier.

        retry_after (:py:obj:`int`, *optional*):
            In case of exceeding flood control, the number of seconds
            left to wait before the request can be repeated.
    """

    def __init__(
        self,
        *,
        migrate_to_chat_id: Optional[int] = None,
        retry_after: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.migrate_to_chat_id = migrate_to_chat_id
        self.retry_after = retry_after

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ResponseParameters"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
