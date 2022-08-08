from typing import Union, List, Optional

from pybotgram import types
from .object import Object


class InputMedia(Object):
    """This object represents the content of a media message to be sent. It
    should be one of
    - :obj:`~pybotgram.types.InputMediaAnimation`
    - :obj:`~pybotgram.types.InputMediaDocument`
    - :obj:`~pybotgram.types.InputMediaAudio`
    - :obj:`~pybotgram.types.InputMediaPhoto`
    - :obj:`~pybotgram.types.InputMediaVideo`
    """

    def __init__(
        self,
        type: str,
        media: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
    ):
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities


class InputMediaPhoto(InputMedia):
    """Represents a photo to be sent.

    Parameters:
        media (:py:obj:`str`):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        caption (:py:obj:`str`, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.
    """

    def __init__(
        self,
        *,
        media: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None
    ):
        super().__init__(
            type="photo",
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )


class InputMediaVideo(InputMedia):
    """Represents a video to be sent.

    Parameters:
        media (:py:obj:`str`):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (:obj:`~pybotgram.types.InputFile` | :py:obj:`str`, *optional*):
            Thumbnail of the file sent; can be ignored if thumbnail
            generation for the file is supported server-side. The
            thumbnail should be in JPEG format and less than 200 kB in
            size. A thumbnail's width and height should not exceed
            320. Ignored if the file is not uploaded using
            multipart/form-data. Thumbnails can't be reused and can be
            only uploaded as a new file, so you can pass
            "attach://<file_attach_name>" if the thumbnail was
            uploaded using multipart/form-data under
            <file_attach_name>. More information on Sending Files ».

        caption (:py:obj:`str`, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        width (:py:obj:`int`, *optional*):
            Video width.

        height (:py:obj:`int`, *optional*):
            Video height.

        duration (:py:obj:`int`, *optional*):
            Video duration in seconds.

        supports_streaming (:py:obj:`bool`, *optional*):
            Pass True, if the uploaded video is suitable for
            streaming.
    """

    def __init__(
        self,
        *,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        supports_streaming: Optional[bool] = None
    ):
        super().__init__(
            type="video",
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )

        self.thumb = thumb
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming


class InputMediaAnimation(InputMedia):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound) to be sent.

    Parameters:
        media (:py:obj:`str`):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (:obj:`~pybotgram.types.InputFile` | :py:obj:`str`, *optional*):
            Thumbnail of the file sent; can be ignored if thumbnail
            generation for the file is supported server-side. The
            thumbnail should be in JPEG format and less than 200 kB in
            size. A thumbnail's width and height should not exceed
            320. Ignored if the file is not uploaded using
            multipart/form-data. Thumbnails can't be reused and can be
            only uploaded as a new file, so you can pass
            "attach://<file_attach_name>" if the thumbnail was
            uploaded using multipart/form-data under
            <file_attach_name>. More information on Sending Files ».

        caption (:py:obj:`str`, *optional*):
            Caption of the animation to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the animation caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        width (:py:obj:`int`, *optional*):
            Animation width.

        height (:py:obj:`int`, *optional*):
            Animation height.

        duration (:py:obj:`int`, *optional*):
            Animation duration in seconds.
    """

    def __init__(
        self,
        *,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None
    ):
        super().__init__(
            type="animation",
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )

        self.thumb = thumb
        self.width = width
        self.height = height
        self.duration = duration


class InputMediaAudio(InputMedia):
    """Represents an audio file to be treated as music to be sent.

    Parameters:
        media (:py:obj:`str`):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (:obj:`~pybotgram.types.InputFile` | :py:obj:`str`, *optional*):
            Thumbnail of the file sent; can be ignored if thumbnail
            generation for the file is supported server-side. The
            thumbnail should be in JPEG format and less than 200 kB in
            size. A thumbnail's width and height should not exceed
            320. Ignored if the file is not uploaded using
            multipart/form-data. Thumbnails can't be reused and can be
            only uploaded as a new file, so you can pass
            "attach://<file_attach_name>" if the thumbnail was
            uploaded using multipart/form-data under
            <file_attach_name>. More information on Sending Files ».

        caption (:py:obj:`str`, *optional*):
            Caption of the audio to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        duration (:py:obj:`int`, *optional*):
            Duration of the audio in seconds.

        performer (:py:obj:`str`, *optional*):
            Performer of the audio.

        title (:py:obj:`str`, *optional*):
            Title of the audio.
    """

    def __init__(
        self,
        *,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None
    ):
        super().__init__(
            type="audio",
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )

        self.thumb = thumb
        self.duration = duration
        self.performer = performer
        self.title = title


class InputMediaDocument(InputMedia):
    """Represents a general file to be sent.

    Parameters:
        media (:py:obj:`str`):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (:obj:`~pybotgram.types.InputFile` | :py:obj:`str`, *optional*):
            Thumbnail of the file sent; can be ignored if thumbnail
            generation for the file is supported server-side. The
            thumbnail should be in JPEG format and less than 200 kB in
            size. A thumbnail's width and height should not exceed
            320. Ignored if the file is not uploaded using
            multipart/form-data. Thumbnails can't be reused and can be
            only uploaded as a new file, so you can pass
            "attach://<file_attach_name>" if the thumbnail was
            uploaded using multipart/form-data under
            <file_attach_name>. More information on Sending Files ».

        caption (:py:obj:`str`, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        disable_content_type_detection (:py:obj:`bool`, *optional*):
            Disables automatic server-side content type detection for
            files uploaded using multipart/form-data. Always True, if
            the document is sent as part of an album.
    """

    def __init__(
        self,
        *,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        disable_content_type_detection: Optional[bool] = None
    ):
        super().__init__(
            type="document",
            media=media,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
        )

        self.thumb = thumb
        self.disable_content_type_detection = disable_content_type_detection
