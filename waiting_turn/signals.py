from .models import WaitingTurn
from .serializers import WaitingTurnSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
import channels.layers
from asgiref.sync import async_to_sync

@receiver(post_save, sender=WaitingTurn)
def create_waiting_turn(sender, instance, created, update_fields, **kwargs):
    turn_id = instance.id
    turn_status = instance.status
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "turns_turns",
        {
            "type": "send_turns",
            "id": turn_id,
            "status": turn_status,
        },
    )



