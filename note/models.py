from django.db import models


class Note(models.Model):
    user = models.ForeignKey('people.People', on_delete=models.CASCADE)
    total_cost = models.FloatField()
    date = models.CharField(max_length=255)
