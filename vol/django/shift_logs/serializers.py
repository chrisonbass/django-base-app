from rest_framework import serializers
from shift_logs.models import ShiftLog

class ShiftLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShiftLog
        fields = ['url', 'name','log', 'date_created', 'last_modified']
