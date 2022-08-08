from typing import Any, List, Optional

from pybotgram import types
from .object import Object


class InlineQueryResult(Object):
    """This object represents one result of an inline query. Telegram clients
    currently support results of the following 20 types:
    - :obj:`~pybotgram.types.InlineQueryResultCachedDocument`
    - :obj:`~pybotgram.types.InlineQueryResultCachedAudio`
    - :obj:`~pybotgram.types.InlineQueryResultCachedGif`
    - :obj:`~pybotgram.types.InlineQueryResultCachedMpeg4Gif`
    - :obj:`~pybotgram.types.InlineQueryResultCachedPhoto`
    - :obj:`~pybotgram.types.InlineQueryResultCachedSticker`
    - :obj:`~pybotgram.types.InlineQueryResultCachedVideo`
    - :obj:`~pybotgram.types.InlineQueryResultCachedVoice`
    - :obj:`~pybotgram.types.InlineQueryResultArticle`
    - :obj:`~pybotgram.types.InlineQueryResultAudio`
    - :obj:`~pybotgram.types.InlineQueryResultContact`
    - :obj:`~pybotgram.types.InlineQueryResultGame`
    - :obj:`~pybotgram.types.InlineQueryResultDocument`
    - :obj:`~pybotgram.types.InlineQueryResultGif`
    - :obj:`~pybotgram.types.InlineQueryResultLocation`
    - :obj:`~pybotgram.types.InlineQueryResultMpeg4Gif`
    - :obj:`~pybotgram.types.InlineQueryResultPhoto`
    - :obj:`~pybotgram.types.InlineQueryResultVenue`
    - :obj:`~pybotgram.types.InlineQueryResultVideo`
    - :obj:`~pybotgram.types.InlineQueryResultVoice`

    Note: All URLs passed in inline query results will be available
    to end users and therefore must be assumed to be public.
    """

    def __init__(self, *, type: str, id: str, **_kwargs: Any):
        super().__init__()

        self.type = type
        self.id = id


class InlineQueryResultArticle(InlineQueryResult):
    """Represents a link to an article or web page.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 Bytes.

        title (:py:obj:`str`):
            Title of the result.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`):
            Content of the message to be sent.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        url (:py:obj:`str`, *optional*):
            URL of the result.

        hide_url (:py:obj:`bool`, *optional*):
            Pass True, if you don't want the URL to be shown in the
            message.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        thumb_url (:py:obj:`str`, *optional*):
            Url of the thumbnail for the result.

        thumb_width (:py:obj:`int`, *optional*):
            Thumbnail width.

        thumb_height (:py:obj:`int`, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        id: str,
        title: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        url: Optional[str] = None,
        hide_url: Optional[bool] = None,
        description: Optional[str] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None
    ):
        super().__init__(type="article", id=id)

        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultPhoto(InlineQueryResult):
    """Represents a link to a photo. By default, this photo will be sent by
    the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the photo.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        photo_url (:py:obj:`str`):
            A valid URL of the photo. Photo must be in JPEG format.
            Photo size must not exceed 5MB.

        thumb_url (:py:obj:`str`):
            URL of the thumbnail for the photo.

        photo_width (:py:obj:`int`, *optional*):
            Width of the photo.

        photo_height (:py:obj:`int`, *optional*):
            Height of the photo.

        title (:py:obj:`str`, *optional*):
            Title for the result.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
        self,
        *,
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
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="photo", id=id)

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


class InlineQueryResultGif(InlineQueryResult):
    """Represents a link to an animated GIF file. By default, this animated
    GIF file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        gif_url (:py:obj:`str`):
            A valid URL for the GIF file. File size must not exceed
            1MB.

        gif_width (:py:obj:`int`, *optional*):
            Width of the GIF.

        gif_height (:py:obj:`int`, *optional*):
            Height of the GIF.

        gif_duration (:py:obj:`int`, *optional*):
            Duration of the GIF in seconds.

        thumb_url (:py:obj:`str`):
            URL of the static (JPEG or GIF) or animated (MPEG4)
            thumbnail for the result.

        thumb_mime_type (:py:obj:`str`, *optional*):
            MIME type of the thumbnail, must be one of "image/jpeg",
            "image/gif", or "video/mp4". Defaults to "image/jpeg".

        title (:py:obj:`str`, *optional*):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the GIF file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the GIF
            animation.
    """

    def __init__(
        self,
        *,
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
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="gif", id=id)

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


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound). By default, this animated MPEG-4 file will be sent by the
    user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the animation.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        mpeg4_url (:py:obj:`str`):
            A valid URL for the MPEG4 file. File size must not exceed
            1MB.

        mpeg4_width (:py:obj:`int`, *optional*):
            Video width.

        mpeg4_height (:py:obj:`int`, *optional*):
            Video height.

        mpeg4_duration (:py:obj:`int`, *optional*):
            Video duration in seconds.

        thumb_url (:py:obj:`str`):
            URL of the static (JPEG or GIF) or animated (MPEG4)
            thumbnail for the result.

        thumb_mime_type (:py:obj:`str`, *optional*):
            MIME type of the thumbnail, must be one of "image/jpeg",
            "image/gif", or "video/mp4". Defaults to "image/jpeg".

        title (:py:obj:`str`, *optional*):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the MPEG-4 file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video
            animation.
    """

    def __init__(
        self,
        *,
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
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="mpeg4_gif", id=id)

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


class InlineQueryResultVideo(InlineQueryResult):
    """Represents a link to a page containing an embedded video player or a
    video file. By default, this video file will be sent by the user
    with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the video.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        video_url (:py:obj:`str`):
            A valid URL for the embedded video player or video file.

        mime_type (:py:obj:`str`):
            MIME type of the content of the video URL, "text/html" or
            "video/mp4".

        thumb_url (:py:obj:`str`):
            URL of the thumbnail (JPEG only) for the video.

        title (:py:obj:`str`):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        video_width (:py:obj:`int`, *optional*):
            Video width.

        video_height (:py:obj:`int`, *optional*):
            Video height.

        video_duration (:py:obj:`int`, *optional*):
            Video duration in seconds.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video.
            This field is required if InlineQueryResultVideo is used
            to send an HTML-page as a result (e.g., a YouTube video).
    """

    def __init__(
        self,
        *,
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
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="video", id=id)

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


class InlineQueryResultAudio(InlineQueryResult):
    """Represents a link to an MP3 audio file. By default, this audio file
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the audio.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        audio_url (:py:obj:`str`):
            A valid URL for the audio file.

        title (:py:obj:`str`):
            Title.

        caption (:py:obj:`str`, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        performer (:py:obj:`str`, *optional*):
            Performer.

        audio_duration (:py:obj:`int`, *optional*):
            Audio duration in seconds.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the audio.
    """

    def __init__(
        self,
        *,
        id: str,
        audio_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        performer: Optional[str] = None,
        audio_duration: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="audio", id=id)

        self.audio_url = audio_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultVoice(InlineQueryResult):
    """Represents a link to a voice recording in an .OGG container encoded
    with OPUS. By default, this voice recording will be sent by the
    user. Alternatively, you can use input_message_content to send a
    message with the specified content instead of the the voice
    message.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        voice_url (:py:obj:`str`):
            A valid URL for the voice recording.

        title (:py:obj:`str`):
            Recording title.

        caption (:py:obj:`str`, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the voice message caption.
            See formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        voice_duration (:py:obj:`int`, *optional*):
            Recording duration in seconds.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the voice
            recording.
    """

    def __init__(
        self,
        *,
        id: str,
        voice_url: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        voice_duration: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="voice", id=id)

        self.voice_url = voice_url
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultDocument(InlineQueryResult):
    """Represents a link to a file. By default, this file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the file. Currently, only .PDF and .ZIP files can be
    sent using this method.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        title (:py:obj:`str`):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        document_url (:py:obj:`str`):
            A valid URL for the file.

        mime_type (:py:obj:`str`):
            MIME type of the content of the file, either
            "application/pdf" or "application/zip".

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the file.

        thumb_url (:py:obj:`str`, *optional*):
            URL of the thumbnail (JPEG only) for the file.

        thumb_width (:py:obj:`int`, *optional*):
            Thumbnail width.

        thumb_height (:py:obj:`int`, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
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
        thumb_height: Optional[int] = None
    ):
        super().__init__(type="document", id=id)

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


class InlineQueryResultLocation(InlineQueryResult):
    """Represents a location on a map. By default, the location will be sent
    by the user. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 Bytes.

        latitude (:py:obj:`float`):
            Location latitude in degrees.

        longitude (:py:obj:`float`):
            Location longitude in degrees.

        title (:py:obj:`str`):
            Location title.

        horizontal_accuracy (:py:obj:`float`, *optional*):
            The radius of uncertainty for the location, measured in
            meters; 0-1500.

        live_period (:py:obj:`int`, *optional*):
            Period in seconds for which the location can be updated,
            should be between 60 and 86400.

        heading (:py:obj:`int`, *optional*):
            For live locations, a direction in which the user is
            moving, in degrees. Must be between 1 and 360 if
            specified.

        proximity_alert_radius (:py:obj:`int`, *optional*):
            For live locations, a maximum distance for proximity
            alerts about approaching another chat member, in meters.
            Must be between 1 and 100000 if specified.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the location.

        thumb_url (:py:obj:`str`, *optional*):
            Url of the thumbnail for the result.

        thumb_width (:py:obj:`int`, *optional*):
            Thumbnail width.

        thumb_height (:py:obj:`int`, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
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
        thumb_height: Optional[int] = None
    ):
        super().__init__(type="location", id=id)

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


class InlineQueryResultVenue(InlineQueryResult):
    """Represents a venue. By default, the venue will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 Bytes.

        latitude (:py:obj:`float`):
            Latitude of the venue location in degrees.

        longitude (:py:obj:`float`):
            Longitude of the venue location in degrees.

        title (:py:obj:`str`):
            Title of the venue.

        address (:py:obj:`str`):
            Address of the venue.

        foursquare_id (:py:obj:`str`, *optional*):
            Foursquare identifier of the venue if known.

        foursquare_type (:py:obj:`str`, *optional*):
            Foursquare type of the venue, if known. (For example,
            "arts_entertainment/default",
            "arts_entertainment/aquarium" or "food/icecream".).

        google_place_id (:py:obj:`str`, *optional*):
            Google Places identifier of the venue.

        google_place_type (:py:obj:`str`, *optional*):
            Google Places type of the venue. (See supported types.).

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the venue.

        thumb_url (:py:obj:`str`, *optional*):
            Url of the thumbnail for the result.

        thumb_width (:py:obj:`int`, *optional*):
            Thumbnail width.

        thumb_height (:py:obj:`int`, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
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
        thumb_height: Optional[int] = None
    ):
        super().__init__(type=type, id=id)

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


class InlineQueryResultContact(InlineQueryResult):
    """Represents a contact with a phone number. By default, this contact
    will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content
    instead of the contact.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 Bytes.

        phone_number (:py:obj:`str`):
            Contact's phone number.

        first_name (:py:obj:`str`):
            Contact's first name.

        last_name (:py:obj:`str`, *optional*):
            Contact's last name.

        vcard (:py:obj:`str`, *optional*):
            Additional data about the contact in the form of a vCard,
            0-2048 bytes.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the contact.

        thumb_url (:py:obj:`str`, *optional*):
            Url of the thumbnail for the result.

        thumb_width (:py:obj:`int`, *optional*):
            Thumbnail width.

        thumb_height (:py:obj:`int`, *optional*):
            Thumbnail height.
    """

    def __init__(
        self,
        *,
        id: str,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None,
        thumb_url: Optional[str] = None,
        thumb_width: Optional[int] = None,
        thumb_height: Optional[int] = None
    ):
        super().__init__(type="contact", id=id)

        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height


class InlineQueryResultGame(InlineQueryResult):
    """Represents a Game.
    Note: This will only work in Telegram versions released after
    October 1, 2016. Older clients will not display any inline results
    if a game result is among them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        game_short_name (:py:obj:`str`):
            Short name of the game.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.
    """

    def __init__(
        self,
        *,
        id: str,
        game_short_name: str,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None
    ):
        super().__init__(type="game", id=id)

        self.game_short_name = game_short_name
        self.reply_markup = reply_markup


class InlineQueryResultCachedPhoto(InlineQueryResult):
    """Represents a link to a photo stored on the Telegram servers. By
    default, this photo will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the photo.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        photo_file_id (:py:obj:`str`):
            A valid file identifier of the photo.

        title (:py:obj:`str`, *optional*):
            Title for the result.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the photo to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the photo caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the photo.
    """

    def __init__(
        self,
        *,
        id: str,
        photo_file_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="photo", id=id)

        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedGif(InlineQueryResult):
    """Represents a link to an animated GIF file stored on the Telegram
    servers. By default, this animated GIF file will be sent by the
    user with an optional caption. Alternatively, you can use
    input_message_content to send a message with specified content
    instead of the animation.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        gif_file_id (:py:obj:`str`):
            A valid file identifier for the GIF file.

        title (:py:obj:`str`, *optional*):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the GIF file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the GIF
            animation.
    """

    def __init__(
        self,
        *,
        id: str,
        gif_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="gif", id=id)

        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without
    sound) stored on the Telegram servers. By default, this animated
    MPEG-4 file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the animation.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        mpeg4_file_id (:py:obj:`str`):
            A valid file identifier for the MPEG4 file.

        title (:py:obj:`str`, *optional*):
            Title for the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the MPEG-4 file to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the caption. See formatting
            options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video
            animation.
    """

    def __init__(
        self,
        *,
        id: str,
        mpeg4_file_id: str,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="mpeg4_gif", id=id)

        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedSticker(InlineQueryResult):
    """Represents a link to a sticker stored on the Telegram servers. By
    default, this sticker will be sent by the user. Alternatively, you
    can use input_message_content to send a message with the specified
    content instead of the sticker.
    Note: This will only work in Telegram versions released after 9
    April, 2016 for static stickers and after 06 July, 2019 for
    animated stickers. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        sticker_file_id (:py:obj:`str`):
            A valid file identifier of the sticker.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the sticker.
    """

    def __init__(
        self,
        *,
        id: str,
        sticker_file_id: str,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="sticker", id=id)

        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedDocument(InlineQueryResult):
    """Represents a link to a file stored on the Telegram servers. By
    default, this file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        title (:py:obj:`str`):
            Title for the result.

        document_file_id (:py:obj:`str`):
            A valid file identifier for the file.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the document to be sent, 0-1024 characters
            after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the document caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the file.
    """

    def __init__(
        self,
        *,
        id: str,
        title: str,
        document_file_id: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="document", id=id)

        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVideo(InlineQueryResult):
    """Represents a link to a video file stored on the Telegram servers. By
    default, this video file will be sent by the user with an optional
    caption. Alternatively, you can use input_message_content to send
    a message with the specified content instead of the video.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        video_file_id (:py:obj:`str`):
            A valid file identifier for the video file.

        title (:py:obj:`str`):
            Title for the result.

        description (:py:obj:`str`, *optional*):
            Short description of the result.

        caption (:py:obj:`str`, *optional*):
            Caption of the video to be sent, 0-1024 characters after
            entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the video caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the video.
    """

    def __init__(
        self,
        *,
        id: str,
        video_file_id: str,
        title: str,
        description: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="video", id=id)

        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedVoice(InlineQueryResult):
    """Represents a link to a voice message stored on the Telegram servers.
    By default, this voice message will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        voice_file_id (:py:obj:`str`):
            A valid file identifier for the voice message.

        title (:py:obj:`str`):
            Voice message title.

        caption (:py:obj:`str`, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the voice message caption.
            See formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the voice
            message.
    """

    def __init__(
        self,
        *,
        id: str,
        voice_file_id: str,
        title: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="voice", id=id)

        self.voice_file_id = voice_file_id
        self.title = title
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content


class InlineQueryResultCachedAudio(InlineQueryResult):
    """Represents a link to an MP3 audio file stored on the Telegram servers.
    By default, this audio file will be sent by the user.
    Alternatively, you can use input_message_content to send a message
    with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9
    April, 2016. Older clients will ignore them.

    Parameters:
        id (:py:obj:`str`):
            Unique identifier for this result, 1-64 bytes.

        audio_file_id (:py:obj:`str`):
            A valid file identifier for the audio file.

        caption (:py:obj:`str`, *optional*):
            Caption, 0-1024 characters after entities parsing.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the audio caption. See
            formatting options for more details.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in the caption,
            which can be specified instead of parse_mode.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message.

        input_message_content (:obj:`~pybotgram.types.InputMessageContent`, *optional*):
            Content of the message to be sent instead of the audio.
    """

    def __init__(
        self,
        *,
        id: str,
        audio_file_id: str,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        input_message_content: Optional["types.InputMessageContent"] = None
    ):
        super().__init__(type="audio", id=id)

        self.audio_file_id = audio_file_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
