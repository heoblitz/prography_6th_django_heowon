from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name="rest_server", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)