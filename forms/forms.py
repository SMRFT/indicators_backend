# forms.py
from django import forms
from rest_framework import serializers

from .models import Register
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


from .models import Login
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =   Login
        fields = '__all__'


from .models import FrontOffice
class FrontOfficeSerializer(forms.ModelForm):
    class Meta:
        model = FrontOffice
        fields = '__all__'


from .models import FirstFloor
class FirstFloorSerializer(forms.ModelForm):
    class Meta:
        model = FirstFloor
        fields = '__all__'


from .models import SecondFloor
class SecondFloorSerializer(forms.ModelForm):
    class Meta:
        model = SecondFloor
        fields = '__all__'


from .models import ThirdFloor
class ThirdFloorSerializer(forms.ModelForm):
    class Meta:
        model = ThirdFloor
        fields = '__all__'

from .models import FirstSuit
class FirstSuitSerializer(forms.ModelForm):
    class Meta:
        model = FirstSuit
        fields = '__all__'


from .models import SecondSuit
class SecondSuitSerializer(forms.ModelForm):
    class Meta:
        model = SecondSuit
        fields = '__all__'


from .models import Lab
class LabSerializer(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'


from .models import CT
class CTSerializer(forms.ModelForm):
    class Meta:
        model = CT
        fields = '__all__'


from .models import MRI
class MRISerializer(forms.ModelForm):
    class Meta:
        model = MRI
        fields = '__all__'


from .models import Xray
class XraySerializer(forms.ModelForm):
    class Meta:
        model = Xray
        fields = '__all__'


from .models import OPD
class OPDSerializer(forms.ModelForm):
    class Meta:
        model = OPD
        fields = '__all__'


from .models import OT
class OTSerializer(forms.ModelForm):
    class Meta:
        model = OT
        fields = '__all__'


from .models import HR
class HRSerializer(forms.ModelForm):
    class Meta:
        model = HR
        fields = '__all__'


from .models import Physiotherapy
class PhysiotherapySerializer(forms.ModelForm):
    class Meta:
        model = Physiotherapy
        fields = '__all__'


from .models import Dialysis
class DialysisSerializer(forms.ModelForm):
    class Meta:
        model = Dialysis
        fields = '__all__'


from .models import EmergencyRoom
class EmergencyRoomSerializer(forms.ModelForm):
    class Meta:
        model = EmergencyRoom
        fields = '__all__'


from .models import MRD
class MRDSerializer(forms.ModelForm):
    class Meta:
        model = MRD
        fields = '__all__'


from .models import ChemoWard
class ChemoWardSerializer(forms.ModelForm):
    class Meta:
        model = ChemoWard
        fields = '__all__'


from .models import RecoveryWard
class RecoveryWardSerializer(forms.ModelForm):
    class Meta:
        model = RecoveryWard
        fields = '__all__'


from .models import SICU
class SICUSerializer(forms.ModelForm):
    class Meta:
        model = SICU
        fields = '__all__'


from .models import MICU
class MICUSerializer(forms.ModelForm):
    class Meta:
        model = MICU
        fields = '__all__'

from .models import NICU
class NICUSerializer(forms.ModelForm):
    class Meta:
        model = NICU
        fields = '__all__'


from .models import FirstFloorRawData
class FirstFloorRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstFloorRawData
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get("request")

        user_identifier = None
        if request:
            user_identifier = request.data.get("auth-user-id")

        validated_data["created_by"] = user_identifier
        validated_data["lastmodified_by"] = user_identifier

        return super().create(validated_data)


from rest_framework import serializers
from .models import (
    FirstSuitRawData,
    SecondFloorRawData,
    SecondSuitRawData,
    ThirdFloorRawData,
    SICURawData,
    MICURawData,
    NICURawData,
    EmergencyRoomRawData,
    ChemoWardRawData,
    RecoverywardRawData,
    OPDRawData
)


class FirstSuitRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstSuitRawData
        fields = "__all__"


class SecondFloorRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondFloorRawData
        fields = "__all__"


class SecondSuitRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSuitRawData
        fields = "__all__"


class ThirdFloorRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdFloorRawData
        fields = "__all__"


class SICURawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SICURawData
        fields = "__all__"


class MICURawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MICURawData
        fields = "__all__"


class NICURawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NICURawData
        fields = "__all__"


class EmergencyRoomRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyRoomRawData
        fields = "__all__"


class ChemoWardRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemoWardRawData
        fields = "__all__"


class RecoverywardRawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoverywardRawData
        fields = "__all__"

class OPDRawDataSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = OPDRawData
        fields = "__all__"
        
    def get_id(self, obj):
        return str(obj.id)  # Convert ObjectId to string

from .models import AvailabilityOfRoomsAndBeds
class AvailabilityOfRoomsAndBedsSerializer(forms.ModelForm):
    class Meta:
        model = AvailabilityOfRoomsAndBeds
        fields = "__all__"


from rest_framework import serializers
from .models import HandHygenieAudit

class HandHygenieAuditSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = HandHygenieAudit
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)  # Convert ObjectId to string

from rest_framework import serializers
from .models import TrainingFeedBack
from bson import ObjectId  # Make sure this is available if using MongoDB

class TrainingFeedBackSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = TrainingFeedBack
        fields = '__all__'

    def get_id(self, obj):
        return str(obj.id)  # Ensures ObjectId is serialized as a string

from .models import Pharmacy
class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

from .models import MockDrill
class MockDrillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockDrill
        fields = '__all__'


from .models import IncidentReport, SupervisorInvestigation

class IncidentReportSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = IncidentReport
        fields = '__all__'

    def get_id(self, obj):
        val = obj.pk or getattr(obj, 'id', None) or getattr(obj, '_id', None)
        return str(val) if val else None


class SupervisorInvestigationSerializer(serializers.ModelSerializer):
    incidentNo = serializers.SerializerMethodField()

    class Meta:
        model = SupervisorInvestigation
        fields = '__all__'

    def get_incidentNo(self, obj):
        incident_id = getattr(obj, 'incidentId', None)
        if not incident_id:
            return "-"
        
        from .models import IncidentReport
        try:
            incident = IncidentReport.objects.filter(incidentNo=incident_id).first()
            if incident:
                return incident.incidentNo
        except Exception:
            pass

        try:
            from bson import ObjectId
            if len(incident_id) == 24:
                from django.conf import settings
                import pymongo
                db_config = settings.DATABASES['default']
                host = db_config.get('CLIENT', {}).get('host', 'mongodb://localhost:27017/')
                db_name = db_config.get('NAME', 'Indicators')
                
                client = pymongo.MongoClient(host)
                db = client[db_name]
                doc = db['forms_incidentreport'].find_one({'_id': ObjectId(incident_id)})
                if doc and 'incidentNo' in doc:
                    return doc['incidentNo']
        except Exception:
            pass

        return incident_id


from .models import IncidentClassification

class IncidentClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentClassification
        fields = '__all__'