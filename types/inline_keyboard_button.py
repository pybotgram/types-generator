from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class InlineKeyboardButton(Object):
    """This object represents one button of an inline keyboard. You must use
    exactly one of the optional fields.

    Parameters:
        text (:py:obj:`str`):
            Label text on the button.

        url (:py:obj:`str`, *optional*):
            HTTP or tg:// URL to be opened when the button is
            pressed. Links tg://user?id=<user_id> can be used to
            mention a user by their ID without using a username, if
            this is allowed by their privacy settings.

        callback_data (:py:obj:`str`, *optional*):
            Data to be sent in a callback query to the bot when
            button is pressed, 1-64 bytes.

        web_app (:obj:`~pybotgram.types.WebAppInfo`, *optional*):
            Description of the Web App that will be launched when the
            user presses the button. The Web App will be able to send
            an arbitrary message on behalf of the user using the
            method answerWebAppQuery. Available only in private chats
            between a user and the bot.

        login_url (:obj:`~pybotgram.types.LoginUrl`, *optional*):
            An HTTPS URL used to automatically authorize the user.
            Can be used as a replacement for the Telegram Login
            Widget.

        switch_inline_query (:py:obj:`str`, *optional*):
            If set, pressing the button will prompt the user to
            select one of their chats, open that chat and insert the
            bot's username and the specified inline query in the input
            field. May be empty, in which case just the bot's username
            will be inserted.  Note: This offers an easy way for users
            to start using your bot in inline mode when they are
            currently in a private chat with it. Especially useful
            when combined with switch_pm… actions - in this case the
            user will be automatically returned to the chat they
            switched from, skipping the chat selection screen.

        switch_inline_query_current_chat (:py:obj:`str`, *optional*):
            If set, pressing the button will insert the bot's
            username and the specified inline query in the current
            chat's input field. May be empty, in which case only the
            bot's username will be inserted.  This offers a quick way
            for the user to open your bot in inline mode in the same
            chat - good for selecting something from multiple options.

        callback_game (:obj:`~pybotgram.types.CallbackGame`, *optional*):
            Description of the game that will be launched when the
            user presses the button.  NOTE: This type of button must
            always be the first button in the first row.

        pay (:py:obj:`bool`, *optional*):
            Specify True, to send a Pay button.  NOTE: This type of
            button must always be the first button in the first row
            and can only be used in invoice messages.
    """

    def __init__(
        self,
        *,
        text: str,
        url: Optional[str] = None,
        callback_data: Optional[str] = None,
        web_app: Optional["types.WebAppInfo"] = None,
        login_url: Optional["types.LoginUrl"] = None,
        switch_inline_query: Optional[str] = None,
        switch_inline_query_current_chat: Optional[str] = None,
        callback_game: Optional["types.CallbackGame"] = None,
        pay: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.web_app = web_app
        self.login_url = login_url
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = (
            switch_inline_query_current_chat
        )
        self.callback_game = callback_game
        self.pay = pay

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["InlineKeyboardButton"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["web_app"] = types.WebAppInfo._parse(data.get("web_app"), bot)
        data["login_url"] = types.LoginUrl._parse(data.get("login_url"), bot)
        data["callback_game"] = types.CallbackGame._parse(
            data.get("callback_game"), bot
        )

        return cls(bot=bot, **data)
