from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet, AlertViewSet

router = routers.DefaultRouter()


router.register(prefix="upload", viewset=UploadViewSet, basename="upload")
router.register(prefix="alerts", viewset=AlertViewSet, basename="alerts")


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('/', include(router.urls)),
]
