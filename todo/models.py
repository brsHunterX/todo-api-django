from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    title = models.CharField(max_length=255, null=False)
    body = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
