from rest_framework import serializers
from .models import Posts
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id')

class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Posts
        fields = (
            'id',
            'title',
            'description',
            'created_at',
        )
        read_only_fields = ('created_at',)