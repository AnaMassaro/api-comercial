from django.db import models


class NoteItem(models.Model):
    note = models.ForeignKey('note.Note', on_delete=models.CASCADE)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    cost = models.FloatField()
    amount = models.IntegerField()