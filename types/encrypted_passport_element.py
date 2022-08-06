from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class EncryptedPassportElement(Object):
    """Describes documents or other Telegram Passport elements shared with
    the bot by the user.

    Parameters:
        type (:py:obj:`str`):
            Element type. One of "personal_details", "passport",
            "driver_license", "identity_card", "internal_passport",
            "address", "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration",
            "temporary_registration", "phone_number", "email".

        data (:py:obj:`str`, *optional*):
            Base64-encoded encrypted Telegram Passport element data
            provided by the user, available for "personal_details",
            "passport", "driver_license", "identity_card",
            "internal_passport" and "address" types. Can be decrypted
            and verified using the accompanying EncryptedCredentials.

        phone_number (:py:obj:`str`, *optional*):
            User's verified phone number, available only for
            "phone_number" type.

        email (:py:obj:`str`, *optional*):
            User's verified email address, available only for "email"
            type.

        files (List of :obj:`~pybotgram.types.PassportFile`, *optional*):
            Array of encrypted files with documents provided by the
            user, available for "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration" and
            "temporary_registration" types. Files can be decrypted and
            verified using the accompanying EncryptedCredentials.

        front_side (:obj:`~pybotgram.types.PassportFile`, *optional*):
            Encrypted file with the front side of the document,
            provided by the user. Available for "passport",
            "driver_license", "identity_card" and "internal_passport".
            The file can be decrypted and verified using the
            accompanying EncryptedCredentials.

        reverse_side (:obj:`~pybotgram.types.PassportFile`, *optional*):
            Encrypted file with the reverse side of the document,
            provided by the user. Available for "driver_license" and
            "identity_card". The file can be decrypted and verified
            using the accompanying EncryptedCredentials.

        selfie (:obj:`~pybotgram.types.PassportFile`, *optional*):
            Encrypted file with the selfie of the user holding a
            document, provided by the user; available for "passport",
            "driver_license", "identity_card" and "internal_passport".
            The file can be decrypted and verified using the
            accompanying EncryptedCredentials.

        translation (List of :obj:`~pybotgram.types.PassportFile`, *optional*):
            Array of encrypted files with translated versions of
            documents provided by the user. Available if requested for
            "passport", "driver_license", "identity_card",
            "internal_passport", "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration" and
            "temporary_registration" types. Files can be decrypted and
            verified using the accompanying EncryptedCredentials.

        hash (:py:obj:`str`):
            Base64-encoded element hash for using in
            PassportElementErrorUnspecified.
    """

    def __init__(
        self,
        *,
        type: str,
        data: Optional[str] = None,
        phone_number: Optional[str] = None,
        email: Optional[str] = None,
        files: Optional[List["types.PassportFile"]] = None,
        front_side: Optional["types.PassportFile"] = None,
        reverse_side: Optional["types.PassportFile"] = None,
        selfie: Optional["types.PassportFile"] = None,
        translation: Optional[List["types.PassportFile"]] = None,
        hash: str,
        **_kwargs: Any
    ):
        super().__init__()

        self.type = type
        self.data = data
        self.phone_number = phone_number
        self.email = email
        self.files = files
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.hash = hash

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["EncryptedPassportElement"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["files"] = types.PassportFile._parse_list(data.get("files"), bot)
        data["front_side"] = types.PassportFile._parse(
            data.get("front_side"), bot
        )
        data["reverse_side"] = types.PassportFile._parse(
            data.get("reverse_side"), bot
        )
        data["selfie"] = types.PassportFile._parse(data.get("selfie"), bot)
        data["translation"] = types.PassportFile._parse_list(
            data.get("translation"), bot
        )

        return cls(bot=bot, **data)
