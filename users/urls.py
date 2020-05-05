from django.urls import path
from users import views
from rest_framework.authtoken.views import obtain_auth_token  # rest login

urlpatterns = [
    path('login', obtain_auth_token, name='api_token_auth'),
    path('register', views.RegisterViewSet.register),
    path('confirm', views.RegisterViewSet.confirm),
    path('create', views.RegisterViewSet.createUser),
    path('info', views.UserViewSet.getUserInfo),
   # path('snippets/<int:pk>/', views.snippet_detail),
]