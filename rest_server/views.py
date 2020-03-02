from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from knox.models import AuthToken

from .serializers import PostSerializer, CreatUserSerializer, UserSerializer, LoginUserSerializer
from .models import Posts

from django.http import JsonResponse

#FBV로 설계하였음
@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
#@permission_classes([IsAuthenticated,])
def posts_list(request):
    # 게시글 리스트 조회
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        queryset = Posts.objects.all()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    '''
    # 게시글 생성 
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def post_create(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    # 요청이 들어오면 PK 객체를 찾는다.
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

# 가입
@api_view(['POST'])
def register_api(request):
    serializer = CreatUserSerializer(data=request.data)

    if len(request.data["username"]) < 5 or len(request.data["username"]) > 12:
        body = {"message" : "id available 5 ~ 11 word"}
        return Response(body, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(
        {
            "user" : UserSerializer(user).data,
            "token" : AuthToken.objects.create(user)[1],
        }
    )

# 로그인
@api_view(['POST'])
def login_api(request):
    serializer = LoginUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data

    return Response(
        {
            "user" : UserSerializer(user).data,
            "token" : AuthToken.objects.create(user)[1],
        }
    )

#로그 아웃
@api_view(['POST'])
def logout_api(request):
    
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

# 로그인 확인
@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def user_status(request):
    serializer = UserSerializer()
    return Response(
        {
            "message" : "인증 되었습니다."
        }
    )

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