from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Posts

from django.http import JsonResponse


@api_view(['GET', 'POST'])
def posts_list(request):
    # 게시글 리스트 조회
    if request.method == 'GET':
        queryset = Posts.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    # 게시글 생성 
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 해당 PK 게시글 조회
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # 해당 PK 게시글 수정
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 해당 PK 게시글 삭제
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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