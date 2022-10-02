from django.contrib.auth.models import User
from django.db import models

class Card(models.Model):
    task = models.TextField()
    answer = models.TextField()
    created_by = models.ForeignKey(User, related_name="cards", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task