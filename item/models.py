from django.db import models


class Item(models.Model):
    product = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)