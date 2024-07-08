from enum import unique

from django.utils.translation import gettext_lazy as _

from core.enums import DocEnum


@unique
class Alert(DocEnum):
    """
    Alerts
    """

    High = 'HIGH', 'HIGH'
    Low = 'LOW', 'LOW'
    Equal = 'EQUAL', 'EQUAL'


_readable_alert = {
    Alert.High.value: _('HIGH'),
    Alert.Low.value: _('LOW'),
    Alert.Equal.value: _('EQUAL'),
}

ALERT_CHOICES = [(d.value, _readable_alert[d.value]) for d in Alert]
