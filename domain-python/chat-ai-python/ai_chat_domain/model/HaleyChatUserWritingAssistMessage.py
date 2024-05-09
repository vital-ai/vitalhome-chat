
from vital_ai_vitalsigns.model.properties.BooleanProperty import BooleanProperty
from vital_ai_vitalsigns.model.properties.DateTimeProperty import DateTimeProperty
from vital_ai_vitalsigns.model.properties.DoubleProperty import DoubleProperty
from vital_ai_vitalsigns.model.properties.FloatProperty import FloatProperty
from vital_ai_vitalsigns.model.properties.GeoLocationProperty import GeoLocationProperty
from vital_ai_vitalsigns.model.properties.IntegerProperty import IntegerProperty
from vital_ai_vitalsigns.model.properties.LongProperty import LongProperty
from vital_ai_vitalsigns.model.properties.OtherProperty import OtherProperty
from vital_ai_vitalsigns.model.properties.StringProperty import StringProperty
from vital_ai_vitalsigns.model.properties.TruthProperty import TruthProperty
from vital_ai_vitalsigns.model.properties.URIProperty import URIProperty
from ai_chat_domain.model.HaleyChatUserMessage import HaleyChatUserMessage


class HaleyChatUserWritingAssistMessage(HaleyChatUserMessage):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatEditingInstructionsMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatEditingResultContentType', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatEditingResultMessage', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatEditingSourceContentType', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasChatEditingSourceMessage', 'prop_class': StringProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyChatUserWritingAssistMessage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#HaleyChatUserWritingAssistMessage'

