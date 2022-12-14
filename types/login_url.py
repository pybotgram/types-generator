from typing import Optional, Dict, Any

import pybotgram
from .object import Object


class LoginUrl(Object):
    """This object represents a parameter of the inline keyboard button used
    to automatically authorize a user. Serves as a great replacement
    for the Telegram Login Widget when the user is coming from
    Telegram. All the user needs to do is tap/click a button and
    confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.

    Parameters:
        url (:py:obj:`str`):
            An HTTPS URL to be opened with user authorization data
            added to the query string when the button is pressed. If
            the user refuses to provide authorization data, the
            original URL without information about the user will be
            opened. The data added is the same as described in
            Receiving authorization data.  NOTE: You must always check
            the hash of the received data to verify the authentication
            and the integrity of the data as described in Checking
            authorization.

        forward_text (:py:obj:`str`, *optional*):
            New text of the button in forwarded messages.

        bot_username (:py:obj:`str`, *optional*):
            Username of a bot, which will be used for user
            authorization. See Setting up a bot for more details. If
            not specified, the current bot's username will be assumed.
            The url's domain must be the same as the domain linked
            with the bot. See Linking your domain to the bot for more
            details.

        request_write_access (:py:obj:`bool`, *optional*):
            Pass True to request the permission for your bot to send
            messages to the user.
    """

    def __init__(
        self,
        *,
        url: str,
        forward_text: Optional[str] = None,
        bot_username: Optional[str] = None,
        request_write_access: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["LoginUrl"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
