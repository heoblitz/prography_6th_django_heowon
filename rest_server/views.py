from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Posts

from django.http import JsonResponse


class PostView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(requests):
        user_count = Posts.objects.count()
        count = {'count' : user_count}
        return JsonResponse(count)
