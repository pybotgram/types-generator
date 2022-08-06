from typing import Any, Dict, Optional

import pybotgram

from .base import Object


class EncryptedCredentials(Object):
    """Describes data required for decrypting and authenticating
    EncryptedPassportElement. See the Telegram Passport Documentation
    for a complete description of the data decryption and
    authentication processes.

    Parameters:
        data (:py:obj:`str`):
            Base64-encoded encrypted JSON-serialized data with unique
            user's payload, data hashes and secrets required for
            EncryptedPassportElement decryption and authentication.

        hash (:py:obj:`str`):
            Base64-encoded data hash for data authentication.

        secret (:py:obj:`str`):
            Base64-encoded secret, encrypted with the bot's public
            RSA key, required for data decryption.
    """

    def __init__(self, *, data: str, hash: str, secret: str, **_kwargs: Any):
        super().__init__()

        self.data = data
        self.hash = hash
        self.secret = secret

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["EncryptedCredentials"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
