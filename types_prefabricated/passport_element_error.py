from typing import Any, List

from .object import Object


class PassportElementError(Object):
    """This object represents an error in the Telegram Passport element which
    was submitted that should be resolved by the user. It should be
    one of:
    - :obj:`~pybotgram.types.PassportElementErrorDataField`
    - :obj:`~pybotgram.types.PassportElementErrorFrontSide`
    - :obj:`~pybotgram.types.PassportElementErrorReverseSide`
    - :obj:`~pybotgram.types.PassportElementErrorSelfie`
    - :obj:`~pybotgram.types.PassportElementErrorFile`
    - :obj:`~pybotgram.types.PassportElementErrorFiles`
    - :obj:`~pybotgram.types.PassportElementErrorTranslationFile`
    - :obj:`~pybotgram.types.PassportElementErrorTranslationFiles`
    - :obj:`~pybotgram.types.PassportElementErrorUnspecified`
    """

    def __init__(self, source: str, type: str, message: str):
        super().__init__()

        self.source = source
        self.type = type
        self.message = message


class PassportElementErrorDataField(PassportElementError):
    """Represents an issue in one of the data fields that was provided by the
    user. The error is considered resolved when the field's value
    changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            error, one of "personal_details", "passport",
            "driver_license", "identity_card", "internal_passport",
            "address".

        field_name (:py:obj:`str`):
            Name of the data field which has the error.

        data_hash (:py:obj:`str`):
            Base64-encoded data hash.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self,
        *,
        type: str,
        field_name: str,
        data_hash: str,
        message: str,
        **_kwargs: Any
    ):
        super().__init__(source="data", type=type, message=message)

        self.field_name = field_name
        self.data_hash = data_hash


class PassportElementErrorFrontSide(PassportElementError):
    """Represents an issue with the front side of a document. The error is
    considered resolved when the file with the front side of the
    document changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            issue, one of "passport", "driver_license",
            "identity_card", "internal_passport".

        file_hash (:py:obj:`str`):
            Base64-encoded hash of the file with the front side of
            the document.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, file_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="front_side", type=type, message=message)

        self.file_hash = file_hash


class PassportElementErrorReverseSide(PassportElementError):
    """Represents an issue with the reverse side of a document. The error is
    considered resolved when the file with reverse side of the
    document changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            issue, one of "driver_license", "identity_card".

        file_hash (:py:obj:`str`):
            Base64-encoded hash of the file with the reverse side of
            the document.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, file_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="reverse_side", type=type, message=message)

        self.file_hash = file_hash


class PassportElementErrorSelfie(PassportElementError):
    """Represents an issue with the selfie with a document. The error is
    considered resolved when the file with the selfie changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            issue, one of "passport", "driver_license",
            "identity_card", "internal_passport".

        file_hash (:py:obj:`str`):
            Base64-encoded hash of the file with the selfie.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, file_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="selfie", type=type, message=message)

        self.file_hash = file_hash


class PassportElementErrorFile(PassportElementError):
    """Represents an issue with a document scan. The error is considered
    resolved when the file with the document scan changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            issue, one of "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration",
            "temporary_registration".

        file_hash (:py:obj:`str`):
            Base64-encoded file hash.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, file_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="file", type=type, message=message)

        self.file_hash = file_hash


class PassportElementErrorFiles(PassportElementError):
    """Represents an issue with a list of scans. The error is considered
    resolved when the list of files containing the scans changes.

    Parameters:
        type (:py:obj:`str`):
            The section of the user's Telegram Passport which has the
            issue, one of "utility_bill", "bank_statement",
            "rental_agreement", "passport_registration",
            "temporary_registration".

        file_hashes (List of :py:obj:`str`):
            List of base64-encoded file hashes.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self,
        *,
        type: str,
        file_hashes: List[str],
        message: str,
        **_kwargs: Any
    ):
        super().__init__(source="files", type=type, message=message)

        self.file_hashes = file_hashes


class PassportElementErrorTranslationFile(PassportElementError):
    """Represents an issue with one of the files that constitute the
    translation of a document. The error is considered resolved when
    the file changes.

    Parameters:
        type (:py:obj:`str`):
            Type of element of the user's Telegram Passport which has
            the issue, one of "passport", "driver_license",
            "identity_card", "internal_passport", "utility_bill",
            "bank_statement", "rental_agreement",
            "passport_registration", "temporary_registration".

        file_hash (:py:obj:`str`):
            Base64-encoded file hash.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, file_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="translation_file", type=type, message=message)

        self.file_hash = file_hash


class PassportElementErrorTranslationFiles(PassportElementError):
    """Represents an issue with the translated version of a document. The
    error is considered resolved when a file with the document
    translation change.

    Parameters:
        type (:py:obj:`str`):
            Type of element of the user's Telegram Passport which has
            the issue, one of "passport", "driver_license",
            "identity_card", "internal_passport", "utility_bill",
            "bank_statement", "rental_agreement",
            "passport_registration", "temporary_registration".

        file_hashes (List of :py:obj:`str`):
            List of base64-encoded file hashes.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self,
        *,
        type: str,
        file_hashes: List[str],
        message: str,
        **_kwargs: Any
    ):
        super().__init__(
            source="translation_files", type=type, message=message
        )

        self.file_hashes = file_hashes


class PassportElementErrorUnspecified(PassportElementError):
    """Represents an issue in an unspecified place. The error is considered
    resolved when new data is added.

    Parameters:
        type (:py:obj:`str`):
            Type of element of the user's Telegram Passport which has
            the issue.

        element_hash (:py:obj:`str`):
            Base64-encoded element hash.

        message (:py:obj:`str`):
            Error message.
    """

    def __init__(
        self, *, type: str, element_hash: str, message: str, **_kwargs: Any
    ):
        super().__init__(source="unspecified", type=type, message=message)

        self.element_hash = element_hash
