
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


class HaleyChatAccountResourceUsage(VITAL_Node):
    _allowed_properties = [
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageGigabyteTotalStorage', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageS3GigabyteTotalStorage', 'prop_class': DoubleProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageS3TotalFileCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageTaskCompleteDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageTotalFileCount', 'prop_class': LongProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#hasResourceUsageUpdateDateTime', 'prop_class': DateTimeProperty}, 
        {'uri': 'http://vital.ai/ontology/chat-ai#isResourceUsageCurrentUpdate', 'prop_class': BooleanProperty}, 
    ]

    @classmethod
    def get_allowed_properties(cls):
        return super().get_allowed_properties() + HaleyChatAccountResourceUsage._allowed_properties

    @classmethod
    def get_class_uri(cls) -> str:
        return 'http://vital.ai/ontology/chat-ai#HaleyChatAccountResourceUsage'

