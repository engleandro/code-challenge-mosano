from rest_framework.routers import SimpleRouter

from apps.got.apiviews import HouseViewSet, MemberViewSet

app = 'got'

router = SimpleRouter()

router.register(r'houses', HouseViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = []
urlpatterns += router.urls
