from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Posts

from django.http import JsonResponse


@api_view(['GET'])
def posts_list(request):
    # 게시글 리스트 조회
    if request.method == 'GET':
        queryset = Posts.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def posts_detail(request, pk):
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 해당 PK 게시글 조회
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

'''
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
'''