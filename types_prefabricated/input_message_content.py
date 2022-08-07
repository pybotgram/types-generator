from typing import List, Optional

from pybotgram import types
from .object import Object


class InputMessageContent(Object):
    """This object represents the content of a message to be sent as a result
    of an inline query. Telegram clients currently support the
    following 5 types:
    - :obj:`~pybotgram.types.InputTextMessageContent`
    - :obj:`~pybotgram.types.InputLocationMessageContent`
    - :obj:`~pybotgram.types.InputVenueMessageContent`
    - :obj:`~pybotgram.types.InputContactMessageContent`
    - :obj:`~pybotgram.types.InputInvoiceMessageContent`
    """
    
    def __init__(self):
        super().__init__()


class InputTextMessageContent(InputMessageContent):
    """Represents the content of a text message to be sent as the result of
    an inline query.

    Parameters:
        message_text (:py:obj:`str`):
            Text of the message to be sent, 1-4096 characters.

        parse_mode (:py:obj:`str`, *optional*):
            Mode for parsing entities in the message text. See
            formatting options for more details.

        entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            List of special entities that appear in message text,
            which can be specified instead of parse_mode.

        disable_web_page_preview (:py:obj:`bool`, *optional*):
            Disables link previews for links in the sent message.
    """

    def __init__(
        self,
        *,
        message_text: str,
        parse_mode: Optional[str] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
        disable_web_page_preview: Optional[bool] = None
    ):     
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview


class InputLocationMessageContent(InputMessageContent):
    """Represents the content of a location message to be sent as the result
    of an inline query.

    Parameters:
        latitude (:py:obj:`float`):
            Latitude of the location in degrees.

        longitude (:py:obj:`float`):
            Longitude of the location in degrees.

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
    """

    def __init__(
        self,
        *,
        latitude: float,
        longitude: float,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class InputVenueMessageContent(InputMessageContent):
    """Represents the content of a venue message to be sent as the result of
    an inline query.

    Parameters:
        latitude (:py:obj:`float`):
            Latitude of the venue in degrees.

        longitude (:py:obj:`float`):
            Longitude of the venue in degrees.

        title (:py:obj:`str`):
            Name of the venue.

        address (:py:obj:`str`):
            Address of the venue.

        foursquare_id (:py:obj:`str`, *optional*):
            Foursquare identifier of the venue, if known.

        foursquare_type (:py:obj:`str`, *optional*):
            Foursquare type of the venue, if known. (For example,
            "arts_entertainment/default",
            "arts_entertainment/aquarium" or "food/icecream".).

        google_place_id (:py:obj:`str`, *optional*):
            Google Places identifier of the venue.

        google_place_type (:py:obj:`str`, *optional*):
            Google Places type of the venue. (See supported types.).
    """

    def __init__(
        self,
        *,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class InputContactMessageContent(InputMessageContent):
    """Represents the content of a contact message to be sent as the result
    of an inline query.

    Parameters:
        phone_number (:py:obj:`str`):
            Contact's phone number.

        first_name (:py:obj:`str`):
            Contact's first name.

        last_name (:py:obj:`str`, *optional*):
            Contact's last name.

        vcard (:py:obj:`str`, *optional*):
            Additional data about the contact in the form of a vCard,
            0-2048 bytes.
    """

    def __init__(
        self,
        *,
        phone_number: str,
        first_name: str,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class InputInvoiceMessageContent(InputMessageContent):
    """Represents the content of an invoice message to be sent as the result
    of an inline query.

    Parameters:
        title (:py:obj:`str`):
            Product name, 1-32 characters.

        description (:py:obj:`str`):
            Product description, 1-255 characters.

        payload (:py:obj:`str`):
            Bot-defined invoice payload, 1-128 bytes. This will not
            be displayed to the user, use for your internal processes.

        provider_token (:py:obj:`str`):
            Payment provider token, obtained via @BotFather.

        currency (:py:obj:`str`):
            Three-letter ISO 4217 currency code, see more on
            currencies.

        prices (List of :obj:`~pybotgram.types.LabeledPrice`):
            Price breakdown, a JSON-serialized list of components
            (e.g. product price, tax, discount, delivery cost,
            delivery tax, bonus, etc.).

        max_tip_amount (:py:obj:`int`, *optional*):
            The maximum accepted amount for tips in the smallest
            units of the currency (integer, not float/double). For
            example, for a maximum tip of US$ 1.45 pass max_tip_amount
            = 145. See the exp parameter in currencies.json, it shows
            the number of digits past the decimal point for each
            currency (2 for the majority of currencies). Defaults to 0.

        suggested_tip_amounts (List of :py:obj:`int`, *optional*):
            A JSON-serialized array of suggested amounts of tip in
            the smallest units of the currency (integer, not
            float/double). At most 4 suggested tip amounts can be
            specified. The suggested tip amounts must be positive,
            passed in a strictly increased order and must not exceed
            max_tip_amount.

        provider_data (:py:obj:`str`, *optional*):
            A JSON-serialized object for data about the invoice,
            which will be shared with the payment provider. A detailed
            description of the required fields should be provided by
            the payment provider.

        photo_url (:py:obj:`str`, *optional*):
            URL of the product photo for the invoice. Can be a photo
            of the goods or a marketing image for a service.

        photo_size (:py:obj:`int`, *optional*):
            Photo size in bytes.

        photo_width (:py:obj:`int`, *optional*):
            Photo width.

        photo_height (:py:obj:`int`, *optional*):
            Photo height.

        need_name (:py:obj:`bool`, *optional*):
            Pass True, if you require the user's full name to
            complete the order.

        need_phone_number (:py:obj:`bool`, *optional*):
            Pass True, if you require the user's phone number to
            complete the order.

        need_email (:py:obj:`bool`, *optional*):
            Pass True, if you require the user's email address to
            complete the order.

        need_shipping_address (:py:obj:`bool`, *optional*):
            Pass True, if you require the user's shipping address to
            complete the order.

        send_phone_number_to_provider (:py:obj:`bool`, *optional*):
            Pass True, if the user's phone number should be sent to
            provider.

        send_email_to_provider (:py:obj:`bool`, *optional*):
            Pass True, if the user's email address should be sent to
            provider.

        is_flexible (:py:obj:`bool`, *optional*):
            Pass True, if the final price depends on the shipping
            method.
    """

    def __init__(
        self,
        *,
        title: str,
        description: str,
        payload: str,
        provider_token: str,
        currency: str,
        prices: List["types.LabeledPrice"],
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None
    ):     
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_address = need_shipping_address
        self.send_phone_number_to_provider = send_phone_number_to_provider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible