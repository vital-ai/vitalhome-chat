
import datetime
from ai_chat_domain.model.HaleyChatCommand import HaleyChatCommand


class AskConfirmEmailRequest(HaleyChatCommand):
        requestedEmailAddress: str
