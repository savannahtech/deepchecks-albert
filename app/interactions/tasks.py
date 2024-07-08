from celery import shared_task

from .models import LLMInteraction, LLMFile

import csv
import os
from io import StringIO

from django.db import transaction

# @shared_task()
# def task_execute(job_params):

#     assignment = Assignment.objects.get(pk=job_params["db_id"])

#     assignment.sum = assignment.first_term + assignment.second_term

#     assignment.save()


@shared_task()
def read_interactions(file_id):
    file_data = LLMFile.objects.get(pk=file_id)
    file = file_data.file.read().decode('utf-8')
    csv_data = csv.reader(StringIO(file), delimiter=',')
    next(csv_data)
    for row in csv_data:
        input, output = row[1], row[2]

        interaction, _ = LLMInteraction.objects.get_or_create(input_data=input, output_data=output)
        with transaction.atomic():
            transaction.on_commit(lambda: calculate_metrics.delay(interaction.id))
        try:
            os.remove(file_data.file.path)
        except OSError:
            pass


@shared_task()
def calculate_metrics(param_id):

    interaction = LLMInteraction.objects.get(pk=param_id)
    interaction.input_metric = len(interaction.input_data)
    interaction.output_metric = len(interaction.output_data)

    interaction.save()
