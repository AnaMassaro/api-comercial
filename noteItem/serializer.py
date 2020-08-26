from rest_framework import serializers
from noteItem.models import NoteItem


class NoteItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoteItem
        fields = ('id', 'note', 'item', 'cost', 'amount')