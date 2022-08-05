from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class InputMedia(Object):
    """This object represents the content of a media message to be sent. It
    should be one of
    - InputMediaAnimation
    - InputMediaDocument
    - InputMediaAudio
    - InputMediaPhoto
    - InputMediaVideo
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["InputMedia"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_input_media: Dict[str, Type["InputMedia"]] = {}
        _type = data.get("")

        if cls is InputMedia and _type in _type_input_media:
            return _type_input_media[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class InputMediaPhoto(InputMedia):
    """Represents a photo to be sent.

    Parameters:
        type (``str``):
            Type of the result, must be photo.

        media (``str``):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        caption (``str``, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.
    """

    def __init__(
        self,
        *,
        type: str,
        media: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InputMediaPhoto"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)

        return cls(bot=bot, **data)


class InputMediaVideo(InputMedia):
    """Represents a video to be sent.

    Parameters:
        type (``str``):
            Type of the result, must be video.

        media (``str``):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (`~pybotgram.types.InputFile` | ``str``, *optional*):
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

        caption (``str``, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        width (``int``, *optional*):
            Video width.

        height (``int``, *optional*):
            Video height.

        duration (``int``, *optional*):
            Video duration in seconds.

        supports_streaming (``bool``, *optional*):
            Pass True, if the uploaded video is suitable for
            streaming.
    """

    def __init__(
        self,
        *,
        type: str,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        supports_streaming: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.media = media
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.width = width
        self.height = height
        self.duration = duration
        self.supports_streaming = supports_streaming

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InputMediaVideo"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)

        return cls(bot=bot, **data)


class InputMediaAnimation(InputMedia):
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound) to be sent.

    Parameters:
        type (``str``):
            Type of the result, must be animation.

        media (``str``):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (`~pybotgram.types.InputFile` | ``str``, *optional*):
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

        caption (``str``, *optional*):
            Caption of the animation to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the animation caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        width (``int``, *optional*):
            Animation width.

        height (``int``, *optional*):
            Animation height.

        duration (``int``, *optional*):
            Animation duration in seconds.
    """

    def __init__(
        self,
        *,
        type: str,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        duration: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.media = media
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.width = width
        self.height = height
        self.duration = duration

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InputMediaAnimation"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)

        return cls(bot=bot, **data)


class InputMediaAudio(InputMedia):
    """Represents an audio file to be treated as music to be sent.

    Parameters:
        type (``str``):
            Type of the result, must be audio.

        media (``str``):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (`~pybotgram.types.InputFile` | ``str``, *optional*):
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

        caption (``str``, *optional*):
            Caption of the audio to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        duration (``int``, *optional*):
            Duration of the audio in seconds.

        performer (``str``, *optional*):
            Performer of the audio.

        title (``str``, *optional*):
            Title of the audio.
    """

    def __init__(
        self,
        *,
        type: str,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.media = media
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InputMediaAudio"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)

        return cls(bot=bot, **data)


class InputMediaDocument(InputMedia):
    """Represents a general file to be sent.

    Parameters:
        type (``str``):
            Type of the result, must be document.

        media (``str``):
            File to send. Pass a file_id to send a file that exists
            on the Telegram servers (recommended), pass an HTTP URL
            for Telegram to get a file from the Internet, or pass
            "attach://<file_attach_name>" to upload a new one using
            multipart/form-data under <file_attach_name> name. More
            information on Sending Files ».

        thumb (`~pybotgram.types.InputFile` | ``str``, *optional*):
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

        caption (``str``, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        disable_content_type_detection (``bool``, *optional*):
            Disables automatic server-side content type detection for
            files uploaded using multipart/form-data. Always True, if
            the document is sent as part of an album.
    """

    def __init__(
        self,
        *,
        type: str,
        media: str,
        thumb: Optional[Union["types.InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        disable_content_type_detection: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.media = media
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InputMediaDocument"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)

        return cls(bot=bot, **data)