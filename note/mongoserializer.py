from rest_framework import serializers
from note.models import Note


class MongoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('id', 'user', 'total_cost', 'date')