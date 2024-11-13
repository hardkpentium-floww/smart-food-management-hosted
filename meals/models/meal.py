from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import TypeChoices


class Meal(AbstractDateTimeModel):
    id = models.CharField(max_length=250, primary_key=True)
    date = models.DateTimeField()
    type = models.CharField(max_length=250, choices=TypeChoices.get_list_of_tuples(), default="LUNCH")



    def __str__(self):
        return self.id
