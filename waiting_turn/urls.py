from rest_framework import routers
from .api import WaitingTurnViewSet

router = routers.DefaultRouter()
router.register('api/turns', WaitingTurnViewSet, 'turns')
urlpatterns = router.urls