from typing import Optional, Dict, Any

import pybotgram
from .object import Object
from pybotgram import types


class Update(Object):
    """This object represents an incoming update.
    At most one of the optional parameters can be present in any
    given update.

    Parameters:
        update_id (:py:obj:`int`):
            The update's unique identifier. Update identifiers start
            from a certain positive number and increase sequentially.
            This ID becomes especially handy if you're using webhooks,
            since it allows you to ignore repeated updates or to
            restore the correct update sequence, should they get out
            of order. If there are no new updates for at least a week,
            then identifier of the next update will be chosen randomly
            instead of sequentially.

        message (:obj:`~pybotgram.types.Message`, *optional*):
            New incoming message of any kind - text, photo, sticker,
            etc.

        edited_message (:obj:`~pybotgram.types.Message`, *optional*):
            New version of a message that is known to the bot and was
            edited.

        channel_post (:obj:`~pybotgram.types.Message`, *optional*):
            New incoming channel post of any kind - text, photo,
            sticker, etc.

        edited_channel_post (:obj:`~pybotgram.types.Message`, *optional*):
            New version of a channel post that is known to the bot
            and was edited.

        inline_query (:obj:`~pybotgram.types.InlineQuery`, *optional*):
            New incoming inline query.

        chosen_inline_result (:obj:`~pybotgram.types.ChosenInlineResult`, *optional*):
            The result of an inline query that was chosen by a user
            and sent to their chat partner. Please see our
            documentation on the feedback collecting for details on
            how to enable these updates for your bot.

        callback_query (:obj:`~pybotgram.types.CallbackQuery`, *optional*):
            New incoming callback query.

        shipping_query (:obj:`~pybotgram.types.ShippingQuery`, *optional*):
            New incoming shipping query. Only for invoices with
            flexible price.

        pre_checkout_query (:obj:`~pybotgram.types.PreCheckoutQuery`, *optional*):
            New incoming pre-checkout query. Contains full
            information about checkout.

        poll (:obj:`~pybotgram.types.Poll`, *optional*):
            New poll state. Bots receive only updates about stopped
            polls and polls, which are sent by the bot.

        poll_answer (:obj:`~pybotgram.types.PollAnswer`, *optional*):
            A user changed their answer in a non-anonymous poll. Bots
            receive new votes only in polls that were sent by the bot
            itself.

        my_chat_member (:obj:`~pybotgram.types.ChatMemberUpdated`, *optional*):
            The bot's chat member status was updated in a chat. For
            private chats, this update is received only when the bot
            is blocked or unblocked by the user.

        chat_member (:obj:`~pybotgram.types.ChatMemberUpdated`, *optional*):
            A chat member's status was updated in a chat. The bot
            must be an administrator in the chat and must explicitly
            specify "chat_member" in the list of allowed_updates to
            receive these updates.

        chat_join_request (:obj:`~pybotgram.types.ChatJoinRequest`, *optional*):
            A request to join the chat has been sent. The bot must
            have the can_invite_users administrator right in the chat
            to receive these updates.
    """

    def __init__(
        self,
        *,
        update_id: int,
        message: Optional["types.Message"] = None,
        edited_message: Optional["types.Message"] = None,
        channel_post: Optional["types.Message"] = None,
        edited_channel_post: Optional["types.Message"] = None,
        inline_query: Optional["types.InlineQuery"] = None,
        chosen_inline_result: Optional["types.ChosenInlineResult"] = None,
        callback_query: Optional["types.CallbackQuery"] = None,
        shipping_query: Optional["types.ShippingQuery"] = None,
        pre_checkout_query: Optional["types.PreCheckoutQuery"] = None,
        poll: Optional["types.Poll"] = None,
        poll_answer: Optional["types.PollAnswer"] = None,
        my_chat_member: Optional["types.ChatMemberUpdated"] = None,
        chat_member: Optional["types.ChatMemberUpdated"] = None,
        chat_join_request: Optional["types.ChatJoinRequest"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
        self.channel_post = channel_post
        self.edited_channel_post = edited_channel_post
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query
        self.shipping_query = shipping_query
        self.pre_checkout_query = pre_checkout_query
        self.poll = poll
        self.poll_answer = poll_answer
        self.my_chat_member = my_chat_member
        self.chat_member = chat_member
        self.chat_join_request = chat_join_request

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Update"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["message"] = types.Message._parse(data.get("message"), bot)
        data["edited_message"] = types.Message._parse(
            data.get("edited_message"), bot
        )
        data["channel_post"] = types.Message._parse(
            data.get("channel_post"), bot
        )
        data["edited_channel_post"] = types.Message._parse(
            data.get("edited_channel_post"), bot
        )
        data["inline_query"] = types.InlineQuery._parse(
            data.get("inline_query"), bot
        )
        data["chosen_inline_result"] = types.ChosenInlineResult._parse(
            data.get("chosen_inline_result"), bot
        )
        data["callback_query"] = types.CallbackQuery._parse(
            data.get("callback_query"), bot
        )
        data["shipping_query"] = types.ShippingQuery._parse(
            data.get("shipping_query"), bot
        )
        data["pre_checkout_query"] = types.PreCheckoutQuery._parse(
            data.get("pre_checkout_query"), bot
        )
        data["poll"] = types.Poll._parse(data.get("poll"), bot)
        data["poll_answer"] = types.PollAnswer._parse(
            data.get("poll_answer"), bot
        )
        data["my_chat_member"] = types.ChatMemberUpdated._parse(
            data.get("my_chat_member"), bot
        )
        data["chat_member"] = types.ChatMemberUpdated._parse(
            data.get("chat_member"), bot
        )
        data["chat_join_request"] = types.ChatJoinRequest._parse(
            data.get("chat_join_request"), bot
        )

        return cls(bot=bot, **data)
