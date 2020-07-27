from rest_framework import viewsets
from shift_logs.serializers import ShiftLogSerializer
from shift_logs.models import ShiftLog

class ShiftLogViewSet(viewsets.ModelViewSet):
    queryset = ShiftLog.objects.all()
    serializer_class = ShiftLogSerializer

    # Save hook called when saving a Model Instance
    def perform_create(self, serializer):
        # Add owner from Request
        serializer.save(owner=self.request.user)
