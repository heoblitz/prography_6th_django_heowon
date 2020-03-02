from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from knox.views import LogoutView
from . import views

urlpatterns = format_suffix_patterns([
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.posts_detail, name='posts_detail'),
    path('auth/register/', views.register_api, name='register_api'),
    path('auth/login/', views.login_api, name='login_api'),
    path('auth/user/', views.user_status, name='user_status'),
    path('auth/logout/', LogoutView.as_view()),
])