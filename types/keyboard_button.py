from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class KeyboardButton(Object):
    """This object represents one button of the reply keyboard. For simple
    text buttons String can be used instead of this object to specify
    text of the button. Optional fields web_app, request_contact,
    request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work
    in Telegram versions released after 9 April, 2016. Older clients
    will display unsupported message.
    Note: request_poll option will only work in Telegram versions
    released after 23 January, 2020. Older clients will display
    unsupported message.
    Note: web_app option will only work in Telegram versions released
    after 16 April, 2022. Older clients will display unsupported
    message.

    Parameters:
        text (:py:obj:`str`):
            Text of the button. If none of the optional fields are
            used, it will be sent as a message when the button is
            pressed.

        request_contact (:py:obj:`bool`, *optional*):
            If True, the user's phone number will be sent as a
            contact when the button is pressed. Available in private
            chats only.

        request_location (:py:obj:`bool`, *optional*):
            If True, the user's current location will be sent when
            the button is pressed. Available in private chats only.

        request_poll (:obj:`~pybotgram.types.KeyboardButtonPollType`, *optional*):
            If specified, the user will be asked to create a poll and
            send it to the bot when the button is pressed. Available
            in private chats only.

        web_app (:obj:`~pybotgram.types.WebAppInfo`, *optional*):
            If specified, the described Web App will be launched when
            the button is pressed. The Web App will be able to send a
            "web_app_data" service message. Available in private chats
            only.
    """

    def __init__(
        self,
        *,
        text: str,
        request_contact: Optional[bool] = None,
        request_location: Optional[bool] = None,
        request_poll: Optional["types.KeyboardButtonPollType"] = None,
        web_app: Optional["types.WebAppInfo"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.request_poll = request_poll
        self.web_app = web_app

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["KeyboardButton"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["request_poll"] = types.KeyboardButtonPollType._parse(
            data.get("request_poll"), bot
        )
        data["web_app"] = types.WebAppInfo._parse(data.get("web_app"), bot)

        return cls(bot=bot, **data)
