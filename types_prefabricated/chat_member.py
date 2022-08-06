from typing import Any, Dict, Optional, Type

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

    Parameters:
        status (:obj:`str`):
            The member's status in the chat. Can be "creator", "administrator",
            "member", "restricted", "left", "kicked"

        user (:obj:`~pybotgram.types.User`):
            Information about the user.
    """

    def __init__(
        self,
        status: str,
        user: "types.User",
        **_kwargs: Any
    ):
        self.status = status
        self.user = user

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional[Type["ChatMember"]]:
        data = data.copy()
        if not (isinstance(data, dict) and data):
            return None

        data["user"] = types.User._parse(data.get("user"), bot)
        
        _status_chat_member: Dict[str, Type["ChatMember"]] = {
            "creator": ChatMemberOwner,
            "administrator": ChatMemberAdministrator,
            "member": ChatMemberMember,
            "restricted": ChatMemberRestricted,
            "left": ChatMemberLeft,
            "kicked": ChatMemberBanned
        }
        _status = data.get("status")

        if cls is ChatMember and _status in _status_chat_member:
            return _status_chat_member[_status]._parse(data, bot)

        return cls(**data, bot=bot)


class ChatMemberOwner(ChatMember):
    """Represents a chat member that owns the chat and has all administrator
    privileges.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.

        is_anonymous (:py:obj:`bool`):
            True, if the user's presence in the chat is hidden.

        custom_title (:py:obj:`str`, *optional*):
            Custom title for this user.
    """

    def __init__(
        self,
        *,
        user: "types.User",
        is_anonymous: bool,
        custom_title: Optional[str] = None,
        **_kwargs: Any
    ):
        super().__init__(status="creator", user=user)
        
        self.user = user
        self.is_anonymous = is_anonymous
        self.custom_title = custom_title


class ChatMemberAdministrator(ChatMember):
    """Represents a chat member that has some additional privileges.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.

        can_be_edited (:py:obj:`bool`):
            True, if the bot is allowed to edit administrator
            privileges of that user.

        is_anonymous (:py:obj:`bool`):
            True, if the user's presence in the chat is hidden.

        can_manage_chat (:py:obj:`bool`):
            True, if the administrator can access the chat event log,
            chat statistics, message statistics in channels, see
            channel members, see anonymous administrators in
            supergroups and ignore slow mode. Implied by any other
            administrator privilege.

        can_delete_messages (:py:obj:`bool`):
            True, if the administrator can delete messages of other
            users.

        can_manage_video_chats (:py:obj:`bool`):
            True, if the administrator can manage video chats.

        can_restrict_members (:py:obj:`bool`):
            True, if the administrator can restrict, ban or unban
            chat members.

        can_promote_members (:py:obj:`bool`):
            True, if the administrator can add new administrators
            with a subset of their own privileges or demote
            administrators that he has promoted, directly or
            indirectly (promoted by administrators that were appointed
            by the user).

        can_change_info (:py:obj:`bool`):
            True, if the user is allowed to change the chat title,
            photo and other settings.

        can_invite_users (:py:obj:`bool`):
            True, if the user is allowed to invite new users to the
            chat.

        can_post_messages (:py:obj:`bool`, *optional*):
            True, if the administrator can post in the channel;
            channels only.

        can_edit_messages (:py:obj:`bool`, *optional*):
            True, if the administrator can edit messages of other
            users and can pin messages; channels only.

        can_pin_messages (:py:obj:`bool`, *optional*):
            True, if the user is allowed to pin messages; groups and
            supergroups only.

        custom_title (:py:obj:`str`, *optional*):
            Custom title for this user.
    """

    def __init__(
        self,
        *,
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
        super().__init__(status="administrator", user=user)
        
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


class ChatMemberMember(ChatMember):
    """Represents a chat member that has no additional privileges or
    restrictions.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.
    """

    def __init__(
        self,
        *,
        user: "types.User",
        **_kwargs: Any
    ):
        super().__init__(status="member", user=user)
        
        self.user = user


class ChatMemberRestricted(ChatMember):
    """Represents a chat member that is under certain restrictions in the
    chat. Supergroups only.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.

        is_member (:py:obj:`bool`):
            True, if the user is a member of the chat at the moment
            of the request.

        can_change_info (:py:obj:`bool`):
            True, if the user is allowed to change the chat title,
            photo and other settings.

        can_invite_users (:py:obj:`bool`):
            True, if the user is allowed to invite new users to the
            chat.

        can_pin_messages (:py:obj:`bool`):
            True, if the user is allowed to pin messages.

        can_send_messages (:py:obj:`bool`):
            True, if the user is allowed to send text messages,
            contacts, locations and venues.

        can_send_media_messages (:py:obj:`bool`):
            True, if the user is allowed to send audios, documents,
            photos, videos, video notes and voice notes.

        can_send_polls (:py:obj:`bool`):
            True, if the user is allowed to send polls.

        can_send_other_messages (:py:obj:`bool`):
            True, if the user is allowed to send animations, games,
            stickers and use inline bots.

        can_add_web_page_previews (:py:obj:`bool`):
            True, if the user is allowed to add web page previews to
            their messages.

        until_date (:py:obj:`int`):
            Date when restrictions will be lifted for this user; unix
            time. If 0, then the user is restricted forever.
    """

    def __init__(
        self,
        *,
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
        super().__init__(status="restricted", user=user)
        
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


class ChatMemberLeft(ChatMember):
    """Represents a chat member that isn't currently a member of the chat,
    but may join it themselves.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.
    """

    def __init__(
        self,
        *,
        user: "types.User",
        **_kwargs: Any
    ):
        super().__init__(status="left", user=user)
        
        self.user = user


class ChatMemberBanned(ChatMember):
    """Represents a chat member that was banned in the chat and can't return
    to the chat or view chat messages.

    Parameters:
        user (:obj:`~pybotgram.types.User`):
            Information about the user.

        until_date (:py:obj:`int`):
            Date when restrictions will be lifted for this user; unix
            time. If 0, then the user is banned forever.
    """

    def __init__(
        self,
        *,
        user: "types.User",
        until_date: int,
        **_kwargs: Any
    ):
        super().__init__(status="kicked", user=user)
        
        self.user = user
        self.until_date = until_date
