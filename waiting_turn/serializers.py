from rest_framework import serializers
from .models import WaitingTurn

class WaitingTurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingTurn
        fields = ('id', 'status', 'created_at')
        read_only_fields = ('id', 'created_at',)
