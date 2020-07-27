from rest_framework import viewsets
from shift_logs.serializers import ShiftLogSerializer
from shift_logs.models import ShiftLog

class ShiftLogViewSet(viewsets.ModelViewSet):
    queryset = ShiftLog.objects.all()
    serializer_class = ShiftLogSerializer
