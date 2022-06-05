from django.db import models
import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    height = models.FloatField()

    # @property
    # def age(self):
    #     return (datetime.datetime.now().date() - self.date_of_birth
