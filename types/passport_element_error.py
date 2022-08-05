from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class PassportElementError(Object):
    """This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be
    one of:
    - PassportElementErrorDataField
    - PassportElementErrorFrontSide
    - PassportElementErrorReverseSide
    - PassportElementErrorSelfie
    - PassportElementErrorFile
    - PassportElementErrorFiles
    - PassportElementErrorTranslationFile
    - PassportElementErrorTranslationFiles
    - PassportElementErrorUnspecified
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["PassportElementError"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_passport_element_error: Dict[str, Type["PassportElementError"]] = {}
        _type = data.get("")

        if cls is PassportElementError and _type in _type_passport_element_error:
            return _type_passport_element_error[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class PassportElementErrorDataField(PassportElementError):
    """Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value
    changes.

    Parameters:
        source (``str``):
            Error source, must be data.

        type (``str``):
            The section of the user's Telegram Passport which has the
            error, one of "personal_details", "passport",
            "driver_license", "identity_card", "internal_passport",
            "address".

        field_name (``str``):
            Name of the data field which has the error.

        data_hash (``str``):
            Base64-encoded data hash.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        field_name: str,
        data_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.field_name = field_name
        self.data_hash = data_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorDataField"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorFrontSide(PassportElementError):
    """Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the
    document changes.

    Parameters:
        source (``str``):
            Error source, must be front_side.

        type (``str``):
            The section of the user's Telegram Passport which has the
            issue, one of "passport", "driver_license",
            "identity_card", "internal_passport".

        file_hash (``str``):
            Base64-encoded hash of the file with the front side of
            the document.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorFrontSide"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorReverseSide(PassportElementError):
    """Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the
    document changes.

    Parameters:
        source (``str``):
            Error source, must be reverse_side.

        type (``str``):
            The section of the user's Telegram Passport which has the
            issue, one of "driver_license", "identity_card".

        file_hash (``str``):
            Base64-encoded hash of the file with the reverse side of
            the document.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorReverseSide"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorSelfie(PassportElementError):
    """Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.

    Parameters:
        source (``str``):
            Error source, must be selfie.

        type (``str``):
            The section of the user's Telegram Passport which has the
            issue, one of "passport", "driver_license",
            "identity_card", "internal_passport".

        file_hash (``str``):
            Base64-encoded hash of the file with the selfie.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorSelfie"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorFile(PassportElementError):
    """Represents an issue with a document scan. The error is considered
    resolved when the file with the document scan changes.

    Parameters:
        source (``str``):
            Error source, must be file.

        type (``str``):
            The section of the user's Telegram Passport which has the
            issue, one of "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration",
            "temporary_registration".

        file_hash (``str``):
            Base64-encoded file hash.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorFile"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorFiles(PassportElementError):
    """Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.

    Parameters:
        source (``str``):
            Error source, must be files.

        type (``str``):
            The section of the user's Telegram Passport which has the
            issue, one of "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration",
            "temporary_registration".

        file_hashes (List of ``str``):
            List of base64-encoded file hashes.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hashes: List[str],
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorFiles"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorTranslationFile(PassportElementError):
    """Represents an issue with one of the files that constitute the
    translation of a document. The error is considered resolved when
    the file changes.

    Parameters:
        source (``str``):
            Error source, must be translation_file.

        type (``str``):
            Type of element of the user's Telegram Passport which has
            the issue, one of "passport", "driver_license",
            "identity_card", "internal_passport", "utility_bill",
            "bank_statement", "rental_agreement",
            "passport_registration", "temporary_registration".

        file_hash (``str``):
            Base64-encoded file hash.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hash = file_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorTranslationFile"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorTranslationFiles(PassportElementError):
    """Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document
    translation change.

    Parameters:
        source (``str``):
            Error source, must be translation_files.

        type (``str``):
            Type of element of the user's Telegram Passport which has
            the issue, one of "passport", "driver_license",
            "identity_card", "internal_passport", "utility_bill",
            "bank_statement", "rental_agreement",
            "passport_registration", "temporary_registration".

        file_hashes (List of ``str``):
            List of base64-encoded file hashes.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        file_hashes: List[str],
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.file_hashes = file_hashes
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorTranslationFiles"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)


class PassportElementErrorUnspecified(PassportElementError):
    """Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.

    Parameters:
        source (``str``):
            Error source, must be unspecified.

        type (``str``):
            Type of element of the user's Telegram Passport which has
            the issue.

        element_hash (``str``):
            Base64-encoded element hash.

        message (``str``):
            Error message.
    """

    def __init__(
        self,
        *,
        source: str,
        type: str,
        element_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.source = source
        self.type = type
        self.element_hash = element_hash
        self.message = message

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["PassportElementErrorUnspecified"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        return cls(bot=bot, **data)