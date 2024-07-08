from django.conf import settings
from django.http import JsonResponse
from django.utils.timezone import now


def health_view(request, *args, **kwargs):
    """
    Simple view to check if the system is up.
    """

    return JsonResponse({})


def check_view(request, *args, **kwargs):
    """
    Simple view to check if the system is up.
    """

    return JsonResponse(
        data={
            "time": now(),
            "app_name": settings.APP_NAME_DEFAULT,
            "app_release": settings.RELEASE,
            "app_version": settings.VERSION,
        },
    )
