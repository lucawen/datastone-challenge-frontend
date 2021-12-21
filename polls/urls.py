from rest_framework import routers
from polls.views import PollViewSet, OptionViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'choice', OptionViewSet)
