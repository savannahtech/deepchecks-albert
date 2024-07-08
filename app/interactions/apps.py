from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


from core.apps import CoreAppConfig


class InteractionsConfig(CoreAppConfig):
    name = 'interactions'
    verbose_name = _('interactions')
    default = True
