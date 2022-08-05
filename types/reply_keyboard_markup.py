from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ReplyKeyboardMarkup(Object):
    """This object represents a custom keyboard with reply options (see
    Introduction to bots for details and examples).

    Parameters:
        keyboard (List of List of :obj:`~pybotgram.types.KeyboardButton`):
            Array of button rows, each represented by an Array of
            KeyboardButton objects.

        resize_keyboard (:obj:`bool`, *optional*):
            Requests clients to resize the keyboard vertically for
            optimal fit (e.g., make the keyboard smaller if there are
            just two rows of buttons). Defaults to false, in which
            case the custom keyboard is always of the same height as
            the app's standard keyboard.

        one_time_keyboard (:obj:`bool`, *optional*):
            Requests clients to hide the keyboard as soon as it's
            been used. The keyboard will still be available, but
            clients will automatically display the usual letter-
            keyboard in the chat - the user can press a special button
            in the input field to see the custom keyboard again.
            Defaults to false.

        input_field_placeholder (:obj:`str`, *optional*):
            The placeholder to be shown in the input field when the
            keyboard is active; 1-64 characters.

        selective (:obj:`bool`, *optional*):
            Use this parameter if you want to show the keyboard to
            specific users only. Targets: 1) users that are @mentioned
            in the text of the Message object; 2) if the bot's message
            is a reply (has reply_to_message_id), sender of the
            original message.  Example: A user requests to change the
            bot's language, bot replies to the request with a keyboard
            to select the new language. Other users in the group don't
            see the keyboard.
    """

    def __init__(
        self,
        *,
        keyboard: List[List["types.KeyboardButton"]],
        resize_keyboard: Optional[bool] = None,
        one_time_keyboard: Optional[bool] = None,
        input_field_placeholder: Optional[str] = None,
        selective: Optional[bool] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["ReplyKeyboardMarkup"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["keyboard"] = types.KeyboardButton._parse_list(
            data.get("keyboard"), bot
        )

        return cls(bot=bot, **data)
