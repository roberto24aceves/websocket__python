from django.db import models

# Create your models here.
STATUS = (
    ('WAITING', 'WAITING'),
    ('ATTEND', 'ATTEND'),
    ('CANCELED', 'CANCELED'),
    ('ATTENDED', 'ATTENDED')
)

class WaitingTurn(models.Model):

    status = models.CharField(blank=True, null=True, max_length=50, choices=STATUS, default='WAITING')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        db_table = 'waiting_turn'