
import datetime
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class HaleyChatInteraction(VITAL_Node):
        agentInstallURI: str
        chatUpdateTimestamp: datetime
        haleyChatInteractionCategoryURI: str
        haleyChatInteractionModelProviderURI: str
        haleyChatInteractionModelTypeURI: str
        haleyChatInteractionScopeChannelURI: str
        haleyChatInteractionScopeLoginURI: str
        haleyChatInteractionScopeURI: str
        haleyChatInteractionStatusURI: str
        haleyChatInteractionTypeURI: str
        haleyChatQuotaCreditUsed: int
        haleyChatQuotaStatusURI: str
        titleManuallySet: bool

