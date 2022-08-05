from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Chat(Object):
    """This object represents a chat.

    Parameters:
        id (:obj:`int`):
            Unique identifier for this chat. This number may have
            more than 32 significant bits and some programming
            languages may have difficulty/silent defects in
            interpreting it. But it has at most 52 significant bits,
            so a signed 64-bit integer or double-precision float type
            are safe for storing this identifier.

        type (:obj:`str`):
            Type of chat, can be either "private", "group",
            "supergroup" or "channel".

        title (:obj:`str`, *optional*):
            Title, for supergroups, channels and group chats.

        username (:obj:`str`, *optional*):
            Username, for private chats, supergroups and channels if
            available.

        first_name (:obj:`str`, *optional*):
            First name of the other party in a private chat.

        last_name (:obj:`str`, *optional*):
            Last name of the other party in a private chat.

        photo (:obj:`~pybotgram.types.ChatPhoto`, *optional*):
            Chat photo. Returned only in getChat.

        bio (:obj:`str`, *optional*):
            Bio of the other party in a private chat. Returned only
            in getChat.

        has_private_forwards (:obj:`bool`, *optional*):
            True, if privacy settings of the other party in the
            private chat allows to use tg://user?id=<user_id> links
            only in chats with the user. Returned only in getChat.

        join_to_send_messages (:obj:`bool`, *optional*):
            True, if users need to join the supergroup before they
            can send messages. Returned only in getChat.

        join_by_request (:obj:`bool`, *optional*):
            True, if all users directly joining the supergroup need
            to be approved by supergroup administrators. Returned only
            in getChat.

        description (:obj:`str`, *optional*):
            Description, for groups, supergroups and channel chats.
            Returned only in getChat.

        invite_link (:obj:`str`, *optional*):
            Primary invite link, for groups, supergroups and channel
            chats. Returned only in getChat.

        pinned_message (:obj:`~pybotgram.types.Message`, *optional*):
            The most recent pinned message (by sending date).
            Returned only in getChat.

        permissions (:obj:`~pybotgram.types.ChatPermissions`, *optional*):
            Default chat member permissions, for groups and
            supergroups. Returned only in getChat.

        slow_mode_delay (:obj:`int`, *optional*):
            For supergroups, the minimum allowed delay between
            consecutive messages sent by each unpriviledged user; in
            seconds. Returned only in getChat.

        message_auto_delete_time (:obj:`int`, *optional*):
            The time after which all messages sent to the chat will
            be automatically deleted; in seconds. Returned only in
            getChat.

        has_protected_content (:obj:`bool`, *optional*):
            True, if messages from the chat can't be forwarded to
            other chats. Returned only in getChat.

        sticker_set_name (:obj:`str`, *optional*):
            For supergroups, name of group sticker set. Returned only
            in getChat.

        can_set_sticker_set (:obj:`bool`, *optional*):
            True, if the bot can change the group sticker set.
            Returned only in getChat.

        linked_chat_id (:obj:`int`, *optional*):
            Unique identifier for the linked chat, i.e. the
            discussion group identifier for a channel and vice versa;
            for supergroups and channel chats. This identifier may be
            greater than 32 bits and some programming languages may
            have difficulty/silent defects in interpreting it. But it
            is smaller than 52 bits, so a signed 64 bit integer or
            double-precision float type are safe for storing this
            identifier. Returned only in getChat.

        location (:obj:`~pybotgram.types.ChatLocation`, *optional*):
            For supergroups, the location to which the supergroup is
            connected. Returned only in getChat.
    """

    def __init__(
        self,
        *,
        id: int,
        type: str,
        title: Optional[str] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        photo: Optional["types.ChatPhoto"] = None,
        bio: Optional[str] = None,
        has_private_forwards: Optional[bool] = None,
        join_to_send_messages: Optional[bool] = None,
        join_by_request: Optional[bool] = None,
        description: Optional[str] = None,
        invite_link: Optional[str] = None,
        pinned_message: Optional["types.Message"] = None,
        permissions: Optional["types.ChatPermissions"] = None,
        slow_mode_delay: Optional[int] = None,
        message_auto_delete_time: Optional[int] = None,
        has_protected_content: Optional[bool] = None,
        sticker_set_name: Optional[str] = None,
        can_set_sticker_set: Optional[bool] = None,
        linked_chat_id: Optional[int] = None,
        location: Optional["types.ChatLocation"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.bio = bio
        self.has_private_forwards = has_private_forwards
        self.join_to_send_messages = join_to_send_messages
        self.join_by_request = join_by_request
        self.description = description
        self.invite_link = invite_link
        self.pinned_message = pinned_message
        self.permissions = permissions
        self.slow_mode_delay = slow_mode_delay
        self.message_auto_delete_time = message_auto_delete_time
        self.has_protected_content = has_protected_content
        self.sticker_set_name = sticker_set_name
        self.can_set_sticker_set = can_set_sticker_set
        self.linked_chat_id = linked_chat_id
        self.location = location

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Chat"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["photo"] = types.ChatPhoto._parse(data.get("photo"), bot)
        data["pinned_message"] = types.Message._parse(
            data.get("pinned_message"), bot
        )
        data["permissions"] = types.ChatPermissions._parse(
            data.get("permissions"), bot
        )
        data["location"] = types.ChatLocation._parse(data.get("location"), bot)

        return cls(bot=bot, **data)
