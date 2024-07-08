from django.urls import path, include
from . import health

from .views import index

urlpatterns = [
    path("health", view=health.health_view, name="health"),
    path("check", view=health.check_view, name="check"),
    path("", view=index, name="home"),
]
