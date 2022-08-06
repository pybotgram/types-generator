from typing import Optional, List, Dict, Any

import pybotgram
from .object import Object


class WebhookInfo(Object):
    """Describes the current status of a webhook.

    Parameters:
        url (:py:obj:`str`):
            Webhook URL, may be empty if webhook is not set up.

        has_custom_certificate (:py:obj:`bool`):
            True, if a custom certificate was provided for webhook
            certificate checks.

        pending_update_count (:py:obj:`int`):
            Number of updates awaiting delivery.

        ip_address (:py:obj:`str`, *optional*):
            Currently used webhook IP address.

        last_error_date (:py:obj:`int`, *optional*):
            Unix time for the most recent error that happened when
            trying to deliver an update via webhook.

        last_error_message (:py:obj:`str`, *optional*):
            Error message in human-readable format for the most
            recent error that happened when trying to deliver an
            update via webhook.

        last_synchronization_error_date (:py:obj:`int`, *optional*):
            Unix time of the most recent error that happened when
            trying to synchronize available updates with Telegram
            datacenters.

        max_connections (:py:obj:`int`, *optional*):
            The maximum allowed number of simultaneous HTTPS
            connections to the webhook for update delivery.

        allowed_updates (List of :py:obj:`str`, *optional*):
            A list of update types the bot is subscribed to. Defaults
            to all update types except chat_member.
    """

    def __init__(
        self,
        *,
        url: str,
        has_custom_certificate: bool,
        pending_update_count: int,
        ip_address: Optional[str] = None,
        last_error_date: Optional[int] = None,
        last_error_message: Optional[str] = None,
        last_synchronization_error_date: Optional[int] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.ip_address = ip_address
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.last_synchronization_error_date = last_synchronization_error_date
        self.max_connections = max_connections
        self.allowed_updates = allowed_updates

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["WebhookInfo"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        return cls(bot=bot, **data)
