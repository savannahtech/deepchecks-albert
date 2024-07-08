from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

from . import choices


class LLMFile(models.Model):
    file = models.FileField()


class LLMInteraction(models.Model):
    input_data = models.TextField(verbose_name=_('input_data'))
    output_data = models.TextField(verbose_name=_('output_data'))

    input_metric = models.IntegerField(verbose_name=_('input_metric'), default=0)
    output_metric = models.IntegerField(verbose_name=_('output_metric'), default=0)

    def save(self, *args, **kwargs):
        self.create_alerts()

        return super().save(*args, **kwargs)

    def create_alerts(self):
        threshold = 30
        if self.input_metric and self.output_metric:

            new_alert = Alert(llm=self)

            if self.input_metric > threshold:
                new_alert.input_alert = choices.Alert.High.value
            elif self.input_metric < threshold:
                new_alert.input_alert = choices.Alert.Low.value
            else:
                new_alert.input_alert = choices.Alert.Equal.value

            if self.output_metric > threshold:
                new_alert.output_alert = choices.Alert.High.value
            elif self.output_metric < threshold:
                new_alert.output_alert = choices.Alert.Low.value
            else:
                new_alert.output_alert = choices.Alert.Equal.value

            new_alert.save()


class Alert(models.Model):

    llm = models.ForeignKey("LLMInteraction", on_delete=models.DO_NOTHING)

    input_alert = models.TextField(
        choices=choices.ALERT_CHOICES,
        default=choices.Alert.Equal.value,
        verbose_name=_('input_alert'),
    )

    output_alert = models.TextField(
        choices=choices.ALERT_CHOICES,
        default=choices.Alert.Equal.value,
        verbose_name=_('output_alert'),
    )
