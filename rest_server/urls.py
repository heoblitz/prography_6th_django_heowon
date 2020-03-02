from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

'''
post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})

post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
'''
'''
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/count/', PostView.get, name='PostView.get'),
])
'''

urlpatterns = format_suffix_patterns([
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.posts_detail, name='posts_detail'),
    path('auth/register/', views.register_api, name='register_api'),
    path('auth/login/', views.login_api, name='login_api'),
    path('auth/logout/', views.login_api, name='logout_api'),
    path('auth/user/', views.user_status, name='user_status'),
])