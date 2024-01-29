from .models import WaitingTurn
from rest_framework import viewsets, permissions
from .serializers import WaitingTurnSerializer

class WaitingTurnViewSet(viewsets.ModelViewSet):
    queryset = WaitingTurn.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WaitingTurnSerializer