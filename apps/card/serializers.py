from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Card
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = (
            "id",
            "task",
            "answer"
        )