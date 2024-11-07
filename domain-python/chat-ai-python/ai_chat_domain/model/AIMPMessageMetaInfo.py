
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
from vital_ai_vitalsigns.model.VITAL_Node import VITAL_Node


class AIMPMessageMetaInfo(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageChannelHistory', 'prop_class': StringProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageChildChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageParentChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageReceiveDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageRequestURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageSourceChannelURI', 'prop_class': URIProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasMessageURI', 'prop_class': URIProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + AIMPMessageMetaInfo._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#AIMPMessageMetaInfo'
