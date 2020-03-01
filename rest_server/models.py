from django.conf import settings
from django.db import models

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)