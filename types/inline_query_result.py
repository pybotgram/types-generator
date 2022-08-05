from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class InlineQueryResult(Object):
    """This object represents one result of an inline query. Telegram clients
    currently support results of the following 20 types:
    - InlineQueryResultCachedAudio
    - InlineQueryResultCachedDocument
    - InlineQueryResultCachedGif
    - InlineQueryResultCachedMpeg4Gif
    - InlineQueryResultCachedPhoto
    - InlineQueryResultCachedSticker
    - InlineQueryResultCachedVideo
    - InlineQueryResultCachedVoice
    - InlineQueryResultArticle
    - InlineQueryResultAudio
    - InlineQueryResultContact
    - InlineQueryResultGame
    - InlineQueryResultDocument
    - InlineQueryResultGif
    - InlineQueryResultLocation
    - InlineQueryResultMpeg4Gif
    - InlineQueryResultPhoto
    - InlineQueryResultVenue
    - InlineQueryResultVideo
    - InlineQueryResultVoice
    Note: All URLs passed in inline query results will be available
    to end users and therefore must be assumed to be public.
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["InlineQueryResult"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_inline_query_result: Dict[str, Type["InlineQueryResult"]] = {}
        _type = data.get("")

        if cls is InlineQueryResult and _type in _type_inline_query_result:
            return _type_inline_query_result[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class InlineQueryResultArticle(InlineQueryResult):
    """Represents a link to an article or web page.

    Parameters:
        type (``str``):
            Type of the result, must be article.

        id (``str``):
            Unique identifier for this result, 1-64 Bytes.

        title (``str``):
            Title of the result.

        input_message_content (`~pybotgram.types.InputMessageContent`):
            Content of the message to be sent.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        url (``str``, *optional*):
            URL of the result.

        hide_url (``bool``, *optional*):
            Pass True, if you don't want the URL to be shown in the
            message.

        description (``str``, *optional*):
            Short description of the result.

        thumb_url (``str``, *optional*):
            Url of the thumbnail for the result.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        url: Optional[str] = None,
        hide_url: Optional[bool] = None,
        description: Optional[str] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultArticle"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultPhoto(InlineQueryResult):
    """Represents a link to a photo. By default, this photo will be sent by
    the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the photo.

    Parameters:
        type (``str``):
            Type of the result, must be photo.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        photo_url (``str``):
            A valid URL of the photo. Photo must be in JPEG format.
            Photo size must not exceed 5MB.

        thumb_url (``str``):
            URL of the thumbnail for the photo.

        photo_width (``int``, *optional*):
            Width of the photo.

        photo_height (``int``, *optional*):
            Height of the photo.

        title (``str``, *optional*):
            Title for the result.

        description (``str``, *optional*):
            Short description of the result.

        caption (``str``, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        photo_url: str,
        thumb_url: str,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultPhoto"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultGif(InlineQueryResult):
    """Represents a link to an animated GIF file. By default, this animated
    GIF file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.

    Parameters:
        type (``str``):
            Type of the result, must be gif.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        gif_url (``str``):
            A valid URL for the GIF file. File size must not exceed
            1MB.

        gif_width (``int``, *optional*):
            Width of the GIF.

        gif_height (``int``, *optional*):
            Height of the GIF.

        gif_duration (``int``, *optional*):
            Duration of the GIF in seconds.

        thumb_url (``str``):
            URL of the static (JPEG or GIF) or animated (MPEG4)
            thumbnail for the result.

        thumb_mime_type (``str``, *optional*):
            MIME type of the thumbnail, must be one of "image/jpeg",
            "image/gif", or "video/mp4". Defaults to "image/jpeg".

        title (``str``, *optional*):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the GIF file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the GIF
            animation.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        gif_url: str,
        gif_width: Optional[int] = None,
        gif_height: Optional[int] = None,
        gif_duration: Optional[int] = None,
        thumb_url: str,
        thumb_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.gif_duration = gif_duration
        self.thumb_url = thumb_url
        self.thumb_mime_type = thumb_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultGif"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound). By default, this animated MPEG-4 file will be sent by the
    user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the animation.

    Parameters:
        type (``str``):
            Type of the result, must be mpeg4_gif.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        mpeg4_url (``str``):
            A valid URL for the MPEG4 file. File size must not exceed
            1MB.

        mpeg4_width (``int``, *optional*):
            Video width.

        mpeg4_height (``int``, *optional*):
            Video height.

        mpeg4_duration (``int``, *optional*):
            Video duration in seconds.

        thumb_url (``str``):
            URL of the static (JPEG or GIF) or animated (MPEG4)
            thumbnail for the result.

        thumb_mime_type (``str``, *optional*):
            MIME type of the thumbnail, must be one of "image/jpeg",
            "image/gif", or "video/mp4". Defaults to "image/jpeg".

        title (``str``, *optional*):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the MPEG-4 file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video
            animation.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        mpeg4_url: str,
        mpeg4_width: Optional[int] = None,
        mpeg4_height: Optional[int] = None,
        mpeg4_duration: Optional[int] = None,
        thumb_url: str,
        thumb_mime_type: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.mpeg4_duration = mpeg4_duration
        self.thumb_url = thumb_url
        self.thumb_mime_type = thumb_mime_type
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultMpeg4Gif"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultVideo(InlineQueryResult):
    """Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user
    with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the video.

    Parameters:
        type (``str``):
            Type of the result, must be video.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        video_url (``str``):
            A valid URL for the embedded video player or video file.

        mime_type (``str``):
            MIME type of the content of the video URL, "text/html" or
            "video/mp4".

        thumb_url (``str``):
            URL of the thumbnail (JPEG only) for the video.

        title (``str``):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        video_width (``int``, *optional*):
            Video width.

        video_height (``int``, *optional*):
            Video height.

        video_duration (``int``, *optional*):
            Video duration in seconds.

        description (``str``, *optional*):
            Short description of the result.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video.
            This field is required if InlineQueryResultVideo is used
            to send an HTML-page as a result (e.g., a YouTube video).
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        video_url: str,
        mime_type: str,
        thumb_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        video_width: Optional[int] = None,
        video_height: Optional[int] = None,
        video_duration: Optional[int] = None,
        description: Optional[str] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultVideo"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultAudio(InlineQueryResult):
    """Represents a link to an MP3 audio file. By default, this audio file
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the audio.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be audio.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        audio_url (``str``):
            A valid URL for the audio file.

        title (``str``):
            Title.

        caption (``str``, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        performer (``str``, *optional*):
            Performer.

        audio_duration (``int``, *optional*):
            Audio duration in seconds.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the audio.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        audio_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        performer: Optional[str] = None,
        audio_duration: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultAudio"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultVoice(InlineQueryResult):
    """Represents a link to a voice recording in an .OGG container encoded
    with OPUS. By default, this voice recording will be sent by the
    user. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the the voice
    message.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be voice.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        voice_url (``str``):
            A valid URL for the voice recording.

        title (``str``):
            Recording title.

        caption (``str``, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the voice message caption.
            See formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        voice_duration (``int``, *optional*):
            Recording duration in seconds.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the voice
            recording.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        voice_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        voice_duration: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultVoice"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultDocument(InlineQueryResult):
    """Represents a link to a file. By default, this file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the file. Currently, only .PDF and .ZIP files can be
    sent using this method.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be document.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        title (``str``):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        document_url (``str``):
            A valid URL for the file.

        mime_type (``str``):
            MIME type of the content of the file, either
            "application/pdf" or "application/zip".

        description (``str``, *optional*):
            Short description of the result.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the file.

        thumb_url (``str``, *optional*):
            URL of the thumbnail (JPEG only) for the file.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        document_url: str,
        mime_type: str,
        description: Optional[str] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultDocument"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultLocation(InlineQueryResult):
    """Represents a location on a map. By default, the location will be sent
    by the user. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be location.

        id (``str``):
            Unique identifier for this result, 1-64 Bytes.

        latitude (``float``):
            Location latitude in degrees.

        longitude (``float``):
            Location longitude in degrees.

        title (``str``):
            Location title.

        horizontal_accuracy (``float``, *optional*):
            The radius of uncertainty for the location, measured in
            meters; 0-1500.

        live_period (``int``, *optional*):
            Period in seconds for which the location can be updated,
            should be between 60 and 86400.

        heading (``int``, *optional*):
            For live locations, a direction in which the user is
            moving, in degrees. Must be between 1 and 360 if
            specified.

        proximity_alert_radius (``int``, *optional*):
            For live locations, a maximum distance for proximity
            alerts about approaching another chat member, in meters.
            Must be between 1 and 100000 if specified.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the location.

        thumb_url (``str``, *optional*):
            Url of the thumbnail for the result.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultLocation"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultVenue(InlineQueryResult):
    """Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be venue.

        id (``str``):
            Unique identifier for this result, 1-64 Bytes.

        latitude (``float``):
            Latitude of the venue location in degrees.

        longitude (``float``):
            Longitude of the venue location in degrees.

        title (``str``):
            Title of the venue.

        address (``str``):
            Address of the venue.

        foursquare_id (``str``, *optional*):
            Foursquare identifier of the venue if known.

        foursquare_type (``str``, *optional*):
            Foursquare type of the venue, if known. (For example,
            "arts_entertainment/default",
            "arts_entertainment/aquarium" or "food/icecream".).

        google_place_id (``str``, *optional*):
            Google Places identifier of the venue.

        google_place_type (``str``, *optional*):
            Google Places type of the venue. (See supported types.).

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the venue.

        thumb_url (``str``, *optional*):
            Url of the thumbnail for the result.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultVenue"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultContact(InlineQueryResult):
    """Represents a contact with a phone number. By default, this contact
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the contact.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be contact.

        id (``str``):
            Unique identifier for this result, 1-64 Bytes.

        phone_number (``str``):
            Contact's phone number.

        first_name (``str``):
            Contact's first name.

        last_name (``str``, *optional*):
            Contact's last name.

        vcard (``str``, *optional*):
            Additional data about the contact in the form of a vCard,
            0-2048 bytes.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the contact.

        thumb_url (``str``, *optional*):
            Url of the thumbnail for the result.

        thumb_width (``int``, *optional*):
            Thumbnail width.

        thumb_height (``int``, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultContact"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultGame(InlineQueryResult):
    """Represents a Game.
    Note: This will only work in Telegram versions released after
    October 1, 2016. Older clients will not display any inline results
    if a game result is among them.

    Parameters:
        type (``str``):
            Type of the result, must be game.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        game_short_name (``str``):
            Short name of the game.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        game_short_name: str,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultGame"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedPhoto(InlineQueryResult):
    """Represents a link to a photo stored on the Telegram servers. By
    default, this photo will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the photo.

    Parameters:
        type (``str``):
            Type of the result, must be photo.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        photo_file_id (``str``):
            A valid file identifier of the photo.

        title (``str``, *optional*):
            Title for the result.

        description (``str``, *optional*):
            Short description of the result.

        caption (``str``, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        photo_file_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedPhoto"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedGif(InlineQueryResult):
    """Represents a link to an animated GIF file stored on the Telegram
    servers. By default, this animated GIF file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with specified content
    instead of the animation.

    Parameters:
        type (``str``):
            Type of the result, must be gif.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        gif_file_id (``str``):
            A valid file identifier for the GIF file.

        title (``str``, *optional*):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the GIF file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the GIF
            animation.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        gif_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedGif"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers. By default, this animated
    MPEG-4 file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.

    Parameters:
        type (``str``):
            Type of the result, must be mpeg4_gif.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        mpeg4_file_id (``str``):
            A valid file identifier for the MPEG4 file.

        title (``str``, *optional*):
            Title for the result.

        caption (``str``, *optional*):
            Caption of the MPEG-4 file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video
            animation.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedMpeg4Gif"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedSticker(InlineQueryResult):
    """Represents a link to a sticker stored on the Telegram servers. By
    default, this sticker will be sent by the user. Alternatively, you
    can use input_message_content to send a message with the specified
    content instead of the sticker.
    Note: This will only work in Telegram versions released after 9
    April, 2016 for static stickers and after 06 July, 2019 for
    animated stickers. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be sticker.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        sticker_file_id (``str``):
            A valid file identifier of the sticker.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the sticker.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        sticker_file_id: str,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedSticker"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedDocument(InlineQueryResult):
    """Represents a link to a file stored on the Telegram servers. By
    default, this file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be document.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        title (``str``):
            Title for the result.

        document_file_id (``str``):
            A valid file identifier for the file.

        description (``str``, *optional*):
            Short description of the result.

        caption (``str``, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the file.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedDocument"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedVideo(InlineQueryResult):
    """Represents a link to a video file stored on the Telegram servers. By
    default, this video file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the video.

    Parameters:
        type (``str``):
            Type of the result, must be video.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        video_file_id (``str``):
            A valid file identifier for the video file.

        title (``str``):
            Title for the result.

        description (``str``, *optional*):
            Short description of the result.

        caption (``str``, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        video_file_id: str,
        title: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedVideo"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedVoice(InlineQueryResult):
    """Represents a link to a voice message stored on the Telegram servers.
    By default, this voice message will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be voice.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        voice_file_id (``str``):
            A valid file identifier for the voice message.

        title (``str``):
            Voice message title.

        caption (``str``, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the voice message caption.
            See formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the voice
            message.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        voice_file_id: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedVoice"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)


class InlineQueryResultCachedAudio(InlineQueryResult):
    """Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        type (``str``):
            Type of the result, must be audio.

        id (``str``):
            Unique identifier for this result, 1-64 bytes.

        audio_file_id (``str``):
            A valid file identifier for the audio file.

        caption (``str``, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (``str``, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the audio.
    """

    def __init__(
        self,
        *,
        type: str,
        id: str,
        audio_file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.type = type
        self.id = id
        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["InlineQueryResultCachedAudio"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["caption_entities"] = types.MessageEntity._parse_list(data.get("caption_entities"), bot)
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(data.get("reply_markup"), bot)
        data["input_message_content"] = types.InputMessageContent._parse(data.get("input_message_content"), bot)

        return cls(bot=bot, **data)