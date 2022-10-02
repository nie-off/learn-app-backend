from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

