from rest_framework import serializers
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

# 회원가입
class CreatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
    
    def craete(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user

# 접속확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

# 로그인

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("login error")

# 로그아웃

#class LogoutUserSerializer(serializers.Serializer):


# 게시글 CRUD
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