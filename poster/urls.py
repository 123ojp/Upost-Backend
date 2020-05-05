from django.urls import path
from poster import views
from rest_framework.authtoken.views import obtain_auth_token  # rest login

urlpatterns = [
    path('b/', views.BoardViewSet.listBoard),
    path('b/<str:board_id>/',views.BoardViewSet.listPost),
    path('b/<str:board_id>/create',views.PostViewSet.createPost),
    path('p/',views.PostViewSet.listAllPost),
    path('p/<str:post_id>/',views.PostViewSet.getPost),
    path('p/<str:post_id>/like',views.PostViewSet.likePost),
    path('p/<str:post_id>/unlike',views.PostViewSet.unlikePost),
    path('p/<str:post_id>/create',views.PostViewSet.createCommit),
    path('p/<str:post_id>/del',views.PostViewSet.delPost),
    path('p/<str:post_id>/edit',views.PostViewSet.editPost),
    path('c/<str:commit_id>/like',views.CommitViewSet.likeCommit),
    path('c/<str:commit_id>/unlike',views.CommitViewSet.unlikeCommit),
    path('c/<str:commit_id>/del',views.CommitViewSet.delCommit),
    path('c/<str:commit_id>/edit',views.CommitViewSet.editCommit),
   # path('snippets/<int:pk>/', views.snippet_detail),
]