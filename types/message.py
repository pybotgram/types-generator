from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Message(Object):
    """This object represents a message.

    Parameters:
        message_id (:py:obj:`int`):
            Unique message identifier inside this chat.

        from_user (:obj:`~pybotgram.types.User`, *optional*):
            Sender of the message; empty for messages sent to
            channels. For backward compatibility, the field contains a
            fake sender user in non-channel chats, if the message was
            sent on behalf of a chat.

        sender_chat (:obj:`~pybotgram.types.Chat`, *optional*):
            Sender of the message, sent on behalf of a chat. For
            example, the channel itself for channel posts, the
            supergroup itself for messages from anonymous group
            administrators, the linked channel for messages
            automatically forwarded to the discussion group. For
            backward compatibility, the field from contains a fake
            sender user in non-channel chats, if the message was sent
            on behalf of a chat.

        date (:py:obj:`int`):
            Date the message was sent in Unix time.

        chat (:obj:`~pybotgram.types.Chat`):
            Conversation the message belongs to.

        forward_from (:obj:`~pybotgram.types.User`, *optional*):
            For forwarded messages, sender of the original message.

        forward_from_chat (:obj:`~pybotgram.types.Chat`, *optional*):
            For messages forwarded from channels or from anonymous
            administrators, information about the original sender chat.

        forward_from_message_id (:py:obj:`int`, *optional*):
            For messages forwarded from channels, identifier of the
            original message in the channel.

        forward_signature (:py:obj:`str`, *optional*):
            For forwarded messages that were originally sent in
            channels or by an anonymous chat administrator, signature
            of the message sender if present.

        forward_sender_name (:py:obj:`str`, *optional*):
            Sender's name for messages forwarded from users who
            disallow adding a link to their account in forwarded
            messages.

        forward_date (:py:obj:`int`, *optional*):
            For forwarded messages, date the original message was
            sent in Unix time.

        is_automatic_forward (:py:obj:`bool`, *optional*):
            True, if the message is a channel post that was
            automatically forwarded to the connected discussion group.

        reply_to_message (:obj:`~pybotgram.types.Message`, *optional*):
            For replies, the original message. Note that the Message
            object in this field will not contain further
            reply_to_message fields even if it itself is a reply.

        via_bot (:obj:`~pybotgram.types.User`, *optional*):
            Bot through which the message was sent.

        edit_date (:py:obj:`int`, *optional*):
            Date the message was last edited in Unix time.

        has_protected_content (:py:obj:`bool`, *optional*):
            True, if the message can't be forwarded.

        media_group_id (:py:obj:`str`, *optional*):
            The unique identifier of a media message group this
            message belongs to.

        author_signature (:py:obj:`str`, *optional*):
            Signature of the post author for messages in channels, or
            the custom title of an anonymous group administrator.

        text (:py:obj:`str`, *optional*):
            For text messages, the actual UTF-8 text of the message.

        entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            For text messages, special entities like usernames, URLs,
            bot commands, etc. that appear in the text.

        animation (:obj:`~pybotgram.types.Animation`, *optional*):
            Message is an animation, information about the animation.
            For backward compatibility, when this field is set, the
            document field will also be set.

        audio (:obj:`~pybotgram.types.Audio`, *optional*):
            Message is an audio file, information about the file.

        document (:obj:`~pybotgram.types.Document`, *optional*):
            Message is a general file, information about the file.

        photo (List of :obj:`~pybotgram.types.PhotoSize`, *optional*):
            Message is a photo, available sizes of the photo.

        sticker (:obj:`~pybotgram.types.Sticker`, *optional*):
            Message is a sticker, information about the sticker.

        video (:obj:`~pybotgram.types.Video`, *optional*):
            Message is a video, information about the video.

        video_note (:obj:`~pybotgram.types.VideoNote`, *optional*):
            Message is a video note, information about the video
            message.

        voice (:obj:`~pybotgram.types.Voice`, *optional*):
            Message is a voice message, information about the file.

        caption (:py:obj:`str`, *optional*):
            Caption for the animation, audio, document, photo, video
            or voice.

        caption_entities (List of :obj:`~pybotgram.types.MessageEntity`, *optional*):
            For messages with a caption, special entities like
            usernames, URLs, bot commands, etc. that appear in the
            caption.

        contact (:obj:`~pybotgram.types.Contact`, *optional*):
            Message is a shared contact, information about the
            contact.

        dice (:obj:`~pybotgram.types.Dice`, *optional*):
            Message is a dice with random value.

        game (:obj:`~pybotgram.types.Game`, *optional*):
            Message is a game, information about the game. More about
            games ».

        poll (:obj:`~pybotgram.types.Poll`, *optional*):
            Message is a native poll, information about the poll.

        venue (:obj:`~pybotgram.types.Venue`, *optional*):
            Message is a venue, information about the venue. For
            backward compatibility, when this field is set, the
            location field will also be set.

        location (:obj:`~pybotgram.types.Location`, *optional*):
            Message is a shared location, information about the
            location.

        new_chat_members (List of :obj:`~pybotgram.types.User`, *optional*):
            New members that were added to the group or supergroup
            and information about them (the bot itself may be one of
            these members).

        left_chat_member (:obj:`~pybotgram.types.User`, *optional*):
            A member was removed from the group, information about
            them (this member may be the bot itself).

        new_chat_title (:py:obj:`str`, *optional*):
            A chat title was changed to this value.

        new_chat_photo (List of :obj:`~pybotgram.types.PhotoSize`, *optional*):
            A chat photo was change to this value.

        delete_chat_photo (:py:obj:`bool`, *optional*):
            Service message: the chat photo was deleted.

        group_chat_created (:py:obj:`bool`, *optional*):
            Service message: the group has been created.

        supergroup_chat_created (:py:obj:`bool`, *optional*):
            Service message: the supergroup has been created. This
            field can't be received in a message coming through
            updates, because bot can't be a member of a supergroup
            when it is created. It can only be found in
            reply_to_message if someone replies to a very first
            message in a directly created supergroup.

        channel_chat_created (:py:obj:`bool`, *optional*):
            Service message: the channel has been created. This field
            can't be received in a message coming through updates,
            because bot can't be a member of a channel when it is
            created. It can only be found in reply_to_message if
            someone replies to a very first message in a channel.

        message_auto_delete_timer_changed (:obj:`~pybotgram.types.MessageAutoDeleteTimerChanged`, *optional*):
            Service message: auto-delete timer settings changed in
            the chat.

        migrate_to_chat_id (:py:obj:`int`, *optional*):
            The group has been migrated to a supergroup with the
            specified identifier. This number may have more than 32
            significant bits and some programming languages may have
            difficulty/silent defects in interpreting it. But it has
            at most 52 significant bits, so a signed 64-bit integer or
            double-precision float type are safe for storing this
            identifier.

        migrate_from_chat_id (:py:obj:`int`, *optional*):
            The supergroup has been migrated from a group with the
            specified identifier. This number may have more than 32
            significant bits and some programming languages may have
            difficulty/silent defects in interpreting it. But it has
            at most 52 significant bits, so a signed 64-bit integer or
            double-precision float type are safe for storing this
            identifier.

        pinned_message (:obj:`~pybotgram.types.Message`, *optional*):
            Specified message was pinned. Note that the Message
            object in this field will not contain further
            reply_to_message fields even if it is itself a reply.

        invoice (:obj:`~pybotgram.types.Invoice`, *optional*):
            Message is an invoice for a payment, information about
            the invoice. More about payments ».

        successful_payment (:obj:`~pybotgram.types.SuccessfulPayment`, *optional*):
            Message is a service message about a successful payment,
            information about the payment. More about payments ».

        connected_website (:py:obj:`str`, *optional*):
            The domain name of the website on which the user has
            logged in. More about Telegram Login ».

        passport_data (:obj:`~pybotgram.types.PassportData`, *optional*):
            Telegram Passport data.

        proximity_alert_triggered (:obj:`~pybotgram.types.ProximityAlertTriggered`, *optional*):
            Service message. A user in the chat triggered another
            user's proximity alert while sharing Live Location.

        video_chat_scheduled (:obj:`~pybotgram.types.VideoChatScheduled`, *optional*):
            Service message: video chat scheduled.

        video_chat_started (:obj:`~pybotgram.types.VideoChatStarted`, *optional*):
            Service message: video chat started.

        video_chat_ended (:obj:`~pybotgram.types.VideoChatEnded`, *optional*):
            Service message: video chat ended.

        video_chat_participants_invited (:obj:`~pybotgram.types.VideoChatParticipantsInvited`, *optional*):
            Service message: new participants invited to a video chat.

        web_app_data (:obj:`~pybotgram.types.WebAppData`, *optional*):
            Service message: data sent by a Web App.

        reply_markup (:obj:`~pybotgram.types.InlineKeyboardMarkup`, *optional*):
            Inline keyboard attached to the message. login_url
            buttons are represented as ordinary url buttons.
    """

    def __init__(
        self,
        *,
        message_id: int,
        from_user: Optional["types.User"] = None,
        sender_chat: Optional["types.Chat"] = None,
        date: int,
        chat: "types.Chat",
        forward_from: Optional["types.User"] = None,
        forward_from_chat: Optional["types.Chat"] = None,
        forward_from_message_id: Optional[int] = None,
        forward_signature: Optional[str] = None,
        forward_sender_name: Optional[str] = None,
        forward_date: Optional[int] = None,
        is_automatic_forward: Optional[bool] = None,
        reply_to_message: Optional["types.Message"] = None,
        via_bot: Optional["types.User"] = None,
        edit_date: Optional[int] = None,
        has_protected_content: Optional[bool] = None,
        media_group_id: Optional[str] = None,
        author_signature: Optional[str] = None,
        text: Optional[str] = None,
        entities: Optional[List["types.MessageEntity"]] = None,
        animation: Optional["types.Animation"] = None,
        audio: Optional["types.Audio"] = None,
        document: Optional["types.Document"] = None,
        photo: Optional[List["types.PhotoSize"]] = None,
        sticker: Optional["types.Sticker"] = None,
        video: Optional["types.Video"] = None,
        video_note: Optional["types.VideoNote"] = None,
        voice: Optional["types.Voice"] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        contact: Optional["types.Contact"] = None,
        dice: Optional["types.Dice"] = None,
        game: Optional["types.Game"] = None,
        poll: Optional["types.Poll"] = None,
        venue: Optional["types.Venue"] = None,
        location: Optional["types.Location"] = None,
        new_chat_members: Optional[List["types.User"]] = None,
        left_chat_member: Optional["types.User"] = None,
        new_chat_title: Optional[str] = None,
        new_chat_photo: Optional[List["types.PhotoSize"]] = None,
        delete_chat_photo: Optional[bool] = None,
        group_chat_created: Optional[bool] = None,
        supergroup_chat_created: Optional[bool] = None,
        channel_chat_created: Optional[bool] = None,
        message_auto_delete_timer_changed: Optional[
            "types.MessageAutoDeleteTimerChanged"
        ] = None,
        migrate_to_chat_id: Optional[int] = None,
        migrate_from_chat_id: Optional[int] = None,
        pinned_message: Optional["types.Message"] = None,
        invoice: Optional["types.Invoice"] = None,
        successful_payment: Optional["types.SuccessfulPayment"] = None,
        connected_website: Optional[str] = None,
        passport_data: Optional["types.PassportData"] = None,
        proximity_alert_triggered: Optional[
            "types.ProximityAlertTriggered"
        ] = None,
        video_chat_scheduled: Optional["types.VideoChatScheduled"] = None,
        video_chat_started: Optional["types.VideoChatStarted"] = None,
        video_chat_ended: Optional["types.VideoChatEnded"] = None,
        video_chat_participants_invited: Optional[
            "types.VideoChatParticipantsInvited"
        ] = None,
        web_app_data: Optional["types.WebAppData"] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.message_id = message_id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_from_message_id = forward_from_message_id
        self.forward_signature = forward_signature
        self.forward_sender_name = forward_sender_name
        self.forward_date = forward_date
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.text = text
        self.entities = entities
        self.animation = animation
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.video_note = video_note
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.contact = contact
        self.dice = dice
        self.game = game
        self.poll = poll
        self.venue = venue
        self.location = location
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.message_auto_delete_timer_changed = (
            message_auto_delete_timer_changed
        )
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message
        self.invoice = invoice
        self.successful_payment = successful_payment
        self.connected_website = connected_website
        self.passport_data = passport_data
        self.proximity_alert_triggered = proximity_alert_triggered
        self.video_chat_scheduled = video_chat_scheduled
        self.video_chat_started = video_chat_started
        self.video_chat_ended = video_chat_ended
        self.video_chat_participants_invited = video_chat_participants_invited
        self.web_app_data = web_app_data
        self.reply_markup = reply_markup

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Message"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["from_user"] = types.User._parse(data.get("from"), bot)
        data["sender_chat"] = types.Chat._parse(data.get("sender_chat"), bot)
        data["chat"] = types.Chat._parse(data.get("chat"), bot)
        data["forward_from"] = types.User._parse(data.get("forward_from"), bot)
        data["forward_from_chat"] = types.Chat._parse(
            data.get("forward_from_chat"), bot
        )
        data["reply_to_message"] = types.Message._parse(
            data.get("reply_to_message"), bot
        )
        data["via_bot"] = types.User._parse(data.get("via_bot"), bot)
        data["entities"] = types.MessageEntity._parse_list(
            data.get("entities"), bot
        )
        data["animation"] = types.Animation._parse(data.get("animation"), bot)
        data["audio"] = types.Audio._parse(data.get("audio"), bot)
        data["document"] = types.Document._parse(data.get("document"), bot)
        data["photo"] = types.PhotoSize._parse_list(data.get("photo"), bot)
        data["sticker"] = types.Sticker._parse(data.get("sticker"), bot)
        data["video"] = types.Video._parse(data.get("video"), bot)
        data["video_note"] = types.VideoNote._parse(
            data.get("video_note"), bot
        )
        data["voice"] = types.Voice._parse(data.get("voice"), bot)
        data["caption_entities"] = types.MessageEntity._parse_list(
            data.get("caption_entities"), bot
        )
        data["contact"] = types.Contact._parse(data.get("contact"), bot)
        data["dice"] = types.Dice._parse(data.get("dice"), bot)
        data["game"] = types.Game._parse(data.get("game"), bot)
        data["poll"] = types.Poll._parse(data.get("poll"), bot)
        data["venue"] = types.Venue._parse(data.get("venue"), bot)
        data["location"] = types.Location._parse(data.get("location"), bot)
        data["new_chat_members"] = types.User._parse_list(
            data.get("new_chat_members"), bot
        )
        data["left_chat_member"] = types.User._parse(
            data.get("left_chat_member"), bot
        )
        data["new_chat_photo"] = types.PhotoSize._parse_list(
            data.get("new_chat_photo"), bot
        )
        data[
            "message_auto_delete_timer_changed"
        ] = types.MessageAutoDeleteTimerChanged._parse(
            data.get("message_auto_delete_timer_changed"), bot
        )
        data["pinned_message"] = types.Message._parse(
            data.get("pinned_message"), bot
        )
        data["invoice"] = types.Invoice._parse(data.get("invoice"), bot)
        data["successful_payment"] = types.SuccessfulPayment._parse(
            data.get("successful_payment"), bot
        )
        data["passport_data"] = types.PassportData._parse(
            data.get("passport_data"), bot
        )
        data[
            "proximity_alert_triggered"
        ] = types.ProximityAlertTriggered._parse(
            data.get("proximity_alert_triggered"), bot
        )
        data["video_chat_scheduled"] = types.VideoChatScheduled._parse(
            data.get("video_chat_scheduled"), bot
        )
        data["video_chat_started"] = types.VideoChatStarted._parse(
            data.get("video_chat_started"), bot
        )
        data["video_chat_ended"] = types.VideoChatEnded._parse(
            data.get("video_chat_ended"), bot
        )
        data[
            "video_chat_participants_invited"
        ] = types.VideoChatParticipantsInvited._parse(
            data.get("video_chat_participants_invited"), bot
        )
        data["web_app_data"] = types.WebAppData._parse(
            data.get("web_app_data"), bot
        )
        data["reply_markup"] = types.InlineKeyboardMarkup._parse(
            data.get("reply_markup"), bot
        )

        return cls(bot=bot, **data)
