from typing import Optional, Dict, List, Any

import pybotgram
from .object import Object
from pybotgram import types


class PassportData(Object):
    """Describes Telegram Passport data shared with the bot by the user.

    Parameters:
        data (List of :obj:`~pybotgram.types.EncryptedPassportElement`):
            Array with information about documents and other Telegram
            Passport elements that was shared with the bot.

        credentials (:obj:`~pybotgram.types.EncryptedCredentials`):
            Encrypted credentials required to decrypt the data.
    """

    def __init__(
        self,
        *,
        data: List["types.EncryptedPassportElement"],
        credentials: "types.EncryptedCredentials",
        **_kwargs: Any
    ):
        super().__init__()

        self.data = data
        self.credentials = credentials

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["PassportData"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["data"] = types.EncryptedPassportElement._parse_list(
            data.get("data"), bot
        )
        data["credentials"] = types.EncryptedCredentials._parse(
            data.get("credentials"), bot
        )

        return cls(bot=bot, **data)
