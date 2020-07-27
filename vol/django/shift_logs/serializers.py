from rest_framework import serializers
from shift_logs.models import ShiftLog

class ShiftLogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_email = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = ShiftLog
        fields = ['url', 'owner', 'owner_email', 'name','log', 'date_created', 'last_modified']
