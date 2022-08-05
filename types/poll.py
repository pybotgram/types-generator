from typing import Any, Dict, List, Optional

import pybotgram
from pybotgram import types

from .base import Object


class Poll(Object):
    """This object contains information about a poll.

    Parameters:
        id (``str``):
            Unique poll identifier.

        question (``str``):
            Poll question, 1-300 characters.

        options (List of `~pybotgram.types.PollOption`):
            List of poll options.

        total_voter_count (``int``):
            Total number of users that voted in the poll.

        is_closed (``bool``):
            True, if the poll is closed.

        is_anonymous (``bool``):
            True, if the poll is anonymous.

        type (``str``):
            Poll type, currently can be "regular" or "quiz".

        allows_multiple_answers (``bool``):
            True, if the poll allows multiple answers.

        correct_option_id (``int``, *optional*):
            0-based identifier of the correct answer option.
            Available only for polls in the quiz mode, which are
            closed, or was sent (not forwarded) by the bot or to the
            private chat with the bot.

        explanation (``str``, *optional*):
            Text that is shown when a user chooses an incorrect
            answer or taps on the lamp icon in a quiz-style poll,
            0-200 characters.

        explanation_entities (List of `~pybotgram.types.MessageEntity`, *optional*):
            Special entities like usernames, URLs, bot commands, etc.
            that appear in the explanation.

        open_period (``int``, *optional*):
            Amount of time in seconds the poll will be active after
            creation.

        close_date (``int``, *optional*):
            Point in time (Unix timestamp) when the poll will be
            automatically closed.
    """

    def __init__(
        self,
        *,
        id: str,
        question: str,
        options: List["types.PollOption"],
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool,
        type: str,
        allows_multiple_answers: bool,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_entities: Optional[List["types.MessageEntity"]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        **_kwargs: Any
    ):
        super().__init__()

        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date

    @classmethod
    def _parse(
        cls, data: Dict[str, Any], bot: "pybotgram.Bot"
    ) -> Optional["Poll"]:
        if not (isinstance(data, dict) and data):
            return None

        data = data.copy()

        data["options"] = types.PollOption._parse_list(
            data.get("options"), bot
        )
        data["explanation_entities"] = types.MessageEntity._parse_list(
            data.get("explanation_entities"), bot
        )

        return cls(bot=bot, **data)
