from django.shortcuts import render
from poster.models import *
from poster.controller import *
from users.models import *
from rest_framework import viewsets
from poster.serializers import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import  permission_classes , api_view ,renderer_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.exceptions import PermissionDenied

# Create your views here.

class BoardViewSet(APIView):
    @api_view(['GET'])
    def listBoard(request):
        
        data = {}
        if request.user.is_authenticated :
            userdetail = UserDetail.objects.get(user=request.user)
            
            myboard = Board.objects.filter(school_id = userdetail.school)
            data['myschool'] = BoardSerializer(myboard, many=True).data
        board = Board.objects.filter(isSchoolBoard=False)
        data['boards'] = BoardSerializer(board, many=True).data
        board = Board.objects.filter(isSchoolBoard=True)
        data['school'] = BoardSerializer(board, many=True).data
        return Response(data)
    @api_view(['GET'])
    def listPost(request,board_id):
        if 'sort_by' in request.GET and request.GET['sort_by'] == 'date':
            post_list = Post.objects.filter(board_id_id = board_id,isDelete=False).order_by('-created_date')
        else:
            from datetime import datetime, timedelta
            tshoursago = datetime.now() - timedelta(hours=36)
            post_list = Post.objects.filter(board_id_id = board_id,isDelete=False,created_date__gte=tshoursago).order_by('-post_likes')
        data = {"posts":[]}
        for post in post_list:
            post = PostController(post.post_id,request.user).getPostOnly()
            data['posts'].append(post)

        return Response(data)
        
#class PostViewSet(viewsets.ModelViewSet):
class PostViewSet(APIView):
    @api_view(['GET'])
    def listAllPost(request):
        if 'sort_by' in request.GET and request.GET['sort_by'] == 'date':
            post_list = Post.objects.filter(isDelete=False).order_by('-created_date')
        else:
            from datetime import datetime, timedelta
            tshoursago = datetime.now() - timedelta(hours=36)
            #post_list = Post.objects.filter(board_id_id = board_id,created_date__gte=tshoursago).order_by('-post_likes')
            post_list = Post.objects.filter(isDelete=False,created_date__gte=tshoursago).order_by('-post_likes')
        
        data = {"posts":[]}
        for post in post_list:
            post = PostController(post.post_id,request.user).getPostOnly()
            data['posts'].append(post)

        return Response(data)
    @api_view(['GET'])  
    def getPost(request,post_id):
        try:
            post = PostController(post_id,request.user).getOnePost()
        except:
            raise PermissionDenied({"message":"No post"})
        
        return Response(post)

    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def likePost(request,post_id):
        post = PostController(post_id,request.user)
        if post.isLike:
            raise PermissionDenied({"message":"You already liked"})
        else:
            post.likePost()

        return Response({"message":"Success"})

    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def unlikePost(request,post_id):
        post = PostController(post_id,request.user)
        if not post.isLike:
            raise PermissionDenied({"message":"You hadn't liked"})
        else :
            post.unlikePost()
        return Response({"message":"Success"})
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def createPost(request,board_id):#{"title":"testagain","text":"test"}
        getboard = Board.objects.get(board_id = board_id)

        if getboard.isSchoolBoard:
            userdetail = UserDetail.objects.get(user=request.user)
            if userdetail.school != getboard.school_id:
                raise PermissionDenied({"message":"You hadn't no Permission create post on this board"})

        new_title = request.data.get('title')
        new_text = request.data.get('text')
        new_post = Post(post_title=new_title, 
                        post_text=new_text,
                        post_author = request.user,
                        board_id_id=board_id)
        new_post.save()
        post_id = new_post.post_id
        return Response({"id":post_id})
    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def createCommit(request,post_id):#{"title":"testagain","text":"test"}
        post = Post.objects.get(post_id = post_id)
        getboard = post.board_id

        if getboard.isSchoolBoard:
            userdetail = UserDetail.objects.get(user=request.user)
            if userdetail.school != getboard.school_id:
                raise PermissionDenied({"message":"You hadn't no Permission create commit on this board"})

        new_text = request.data.get('text')
        new_commit = Commit(
                        text=new_text,
                        author = request.user,
                        post_id_id=post_id)
        new_commit.save()
        commit_id = new_commit.id
        return Response({"id":commit_id})
    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def delPost(request,post_id):
        post = PostController(post_id,request.user)
        if not post.AreUAuthor() :
            raise PermissionDenied({"message":"You can't del"})
        post.delPost()
        return Response({"message":"Success"})
    @api_view(['POST'])  
    @permission_classes([IsAuthenticated])
    def editPost(request,post_id):
        post = PostController(post_id,request.user)
        if not post.AreUAuthor() :
            raise PermissionDenied({"message":"You can't edit"})
        if 'text' not in request.data or 'title' not in request.data:
            raise PermissionDenied({"message":"empty text"})
        new_title = request.data.get('title')
        new_text = request.data.get('text')
        post.editPost(new_title,new_text)
        return Response({"message":"Success"})  

class CommitViewSet(APIView):
    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def likeCommit(request,commit_id):
        commit = CommitController(commit_id,request.user)
        if commit.isLike:
            raise PermissionDenied({"message":"You already liked"})
        else:
            commit.likeCommit()

        return Response({"message":"Success"})

    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def unlikeCommit(request,commit_id):
        commit = CommitController(commit_id,request.user)
        if not commit.isLike:
            raise PermissionDenied({"message":"You hadn't liked"})
        else :
            commit.unlikeCommit()
        return Response({"message":"Success"})
    @api_view(['GET'])  
    @permission_classes([IsAuthenticated])
    def delCommit(request,commit_id):
        commit = CommitController(commit_id,request.user)
        if not commit.AreUAuthor() :
            raise PermissionDenied({"message":"You can't del"})
        commit.delCommit()
        return Response({"message":"Success"})
    @api_view(['POST'])  
    @permission_classes([IsAuthenticated])
    def editCommit(request,commit_id):
        commit = CommitController(commit_id,request.user)
        if not commit.AreUAuthor() :
            raise PermissionDenied({"message":"You can't edit"})
        if 'text' not in request.data:
            raise PermissionDenied({"message":"empty text"})
        new_text = request.data.get('text')
        commit.editCommit(new_text)
        return Response({"message":"Success"})  