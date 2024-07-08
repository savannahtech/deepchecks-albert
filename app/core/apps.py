import logging

from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)
logger.setLevel(settings.LOGGING_LEVEL)


class CoreAppConfig(AppConfig):
    """
    Core AppConfig class with basic ``ready`` method
    """

    def ready(self):
        """
        Simple ``ready`` method. Prints (in debug mode) if app is ready.
        """

        logger.debug(_('Module “{}” started and ready!!!').format(self.get_name()))

    def get_name(self):  # pragma: no cover
        """
        Decides app name from different options
        """

        if self.verbose_name:
            return self.verbose_name
        if self.name:
            return self.name
        return type(self)
