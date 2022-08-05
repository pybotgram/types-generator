from typing import Any, Dict, Optional

import pybotgram
from pybotgram import types

from .base import Object


class ChatMember(Object):
    """This object contains information about one member of a chat.
    Currently, the following 6 types of chat members are supported:
    - ChatMemberOwner
    - ChatMemberAdministrator
    - ChatMemberMember
    - ChatMemberRestricted
    - ChatMemberLeft
    - ChatMemberBanned
    """

    def __init__(
        self,# FIXME
        **_kwargs: Any
    ):
        # FIXME

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["ChatMember"]]:
        if not (isinstance(data, dict) and data):
            return None
        
        _type_chat_member: Dict[str, Type["ChatMember"]] = {}
        _type = data.get("")

        if cls is ChatMember and _type in _type_chat_member:
            return _type_chat_member[_type]._parse(data, bot)

        return cls(**data, bot=bot)


class ChatMemberOwner(ChatMember):
    """Represents a chat member that owns the chat and has all administrator
    privileges.

    Parameters:
        status (``str``):
            The member's status in the chat, always "creator".

        user (`~pybotgram.types.User`):
            Information about the user.

        is_anonymous (``bool``):
            True, if the user's presence in the chat is hidden.

        custom_title (``str``, *optional*):
            Custom title for this user.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        is_anonymous: bool,
        custom_title: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberOwner"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)


class ChatMemberAdministrator(ChatMember):
    """Represents a chat member that has some additional privileges.

    Parameters:
        status (``str``):
            The member's status in the chat, always "administrator".

        user (`~pybotgram.types.User`):
            Information about the user.

        can_be_edited (``bool``):
            True, if the bot is allowed to edit administrator
            privileges of that user.

        is_anonymous (``bool``):
            True, if the user's presence in the chat is hidden.

        can_manage_chat (``bool``):
            True, if the administrator can access the chat event log,
            chat statistics, message statistics in channels, see
            channel members, see anonymous administrators in
            supergroups and ignore slow mode. Implied by any other
            administrator privilege.

        can_delete_messages (``bool``):
            True, if the administrator can delete messages of other
            users.

        can_manage_video_chats (``bool``):
            True, if the administrator can manage video chats.

        can_restrict_members (``bool``):
            True, if the administrator can restrict, ban or unban
            chat members.

        can_promote_members (``bool``):
            True, if the administrator can add new administrators
            with a subset of their own privileges or demote
            administrators that he has promoted, directly or
            indirectly (promoted by administrators that were appointed
            by the user).

        can_change_info (``bool``):
            True, if the user is allowed to change the chat title,
            photo and other settings.

        can_invite_users (``bool``):
            True, if the user is allowed to invite new users to the
            chat.

        can_post_messages (``bool``, *optional*):
            True, if the administrator can post in the channel;
            channels only.

        can_edit_messages (``bool``, *optional*):
            True, if the administrator can edit messages of other
            users and can pin messages; channels only.

        can_pin_messages (``bool``, *optional*):
            True, if the user is allowed to pin messages; groups and
            supergroups only.

        custom_title (``str``, *optional*):
            Custom title for this user.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        can_be_edited: bool,
        is_anonymous: bool,
        can_manage_chat: bool,
        can_delete_messages: bool,
        can_manage_video_chats: bool,
        can_restrict_members: bool,
        can_promote_members: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        custom_title: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user
        self.can_be_edited = can_be_edited
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.custom_title = custom_title

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberAdministrator"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)


class ChatMemberMember(ChatMember):
    """Represents a chat member that has no additional privileges or
    restrictions.

    Parameters:
        status (``str``):
            The member's status in the chat, always "member".

        user (`~pybotgram.types.User`):
            Information about the user.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberMember"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)


class ChatMemberRestricted(ChatMember):
    """Represents a chat member that is under certain restrictions in the
    chat. Supergroups only.

    Parameters:
        status (``str``):
            The member's status in the chat, always "restricted".

        user (`~pybotgram.types.User`):
            Information about the user.

        is_member (``bool``):
            True, if the user is a member of the chat at the moment
            of the request.

        can_change_info (``bool``):
            True, if the user is allowed to change the chat title,
            photo and other settings.

        can_invite_users (``bool``):
            True, if the user is allowed to invite new users to the
            chat.

        can_pin_messages (``bool``):
            True, if the user is allowed to pin messages.

        can_send_messages (``bool``):
            True, if the user is allowed to send text messages,
            contacts, locations and venues.

        can_send_media_messages (``bool``):
            True, if the user is allowed to send audios, documents,
            photos, videos, video notes and voice notes.

        can_send_polls (``bool``):
            True, if the user is allowed to send polls.

        can_send_other_messages (``bool``):
            True, if the user is allowed to send animations, games,
            stickers and use inline bots.

        can_add_web_page_previews (``bool``):
            True, if the user is allowed to add web page previews to
            their messages.

        until_date (``int``):
            Date when restrictions will be lifted for this user; unix
            time. If 0, then the user is restricted forever.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        is_member: bool,
        can_change_info: bool,
        can_invite_users: bool,
        can_pin_messages: bool,
        can_send_messages: bool,
        can_send_media_messages: bool,
        can_send_polls: bool,
        can_send_other_messages: bool,
        can_add_web_page_previews: bool,
        until_date: int,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user
        self.is_member = is_member
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_polls = can_send_polls
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.until_date = until_date

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberRestricted"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)


class ChatMemberLeft(ChatMember):
    """Represents a chat member that isn't currently a member of the chat,
    but may join it themselves.

    Parameters:
        status (``str``):
            The member's status in the chat, always "left".

        user (`~pybotgram.types.User`):
            Information about the user.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberLeft"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)


class ChatMemberBanned(ChatMember):
    """Represents a chat member that was banned in the chat and can't return
    to the chat or view chat messages.

    Parameters:
        status (``str``):
            The member's status in the chat, always "kicked".

        user (`~pybotgram.types.User`):
            Information about the user.

        until_date (``int``):
            Date when restrictions will be lifted for this user; unix
            time. If 0, then the user is banned forever.
    """

    def __init__(
        self,
        *,
        status: str,
        user: "types.User",
        until_date: int,
        **_kwargs: Any
    ):
        super().__init__()
        
        self.status = status
        self.user = user
        self.until_date = until_date

    @classmethod
    def _parse(
        cls, 
        data: Dict[str, Any],
        bot: "pybotgram.Bot"
    ) -> Optional["ChatMemberBanned"]:
        if not (isinstance(data, dict) and data):
            return None
        
        data = data.copy()
        
        data["user"] = types.User._parse(data.get("user"), bot)

        return cls(bot=bot, **data)