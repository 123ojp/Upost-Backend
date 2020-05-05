from poster.models import *
from poster.serializers import *
from users.controller import *

class PostController():
    AUTHOR = 'author'
    POST = 'post'
    COMMIT = 'commit'
    TOPCOMMIT = 'top_commit'
    LIKE = 'like'
    TEXT = 'text'
    TITLE = 'title'
    AUTSEX = 'author_sex'
    CR_DATE = 'create_date'
    BOARD_NA = 'board_name'
    P_ID = 'post_id'
    C_ID = 'commit_id'
    ISLIKE ='is_like'
    IS_D = 'is_del'
    COM_COUNT = 'commit_num'
    IS_AUT = 'is_author'
    def __init__(self,post,user):
        self.id = post
        self.post = Post.objects.get(pk = self.id ) 
        self.user = user
        self.isUser = user.is_authenticated
        self.isAuthor = False
        
        if self.post.isDelete == True:
            self.post = None
        if self.isUser :
            self.isLike = self.isLikeorNot()
            if self.post.post_author == self.user:
                self.isAuthor = True
        else:
            self.isLike = False
    def isLikeorNot(self):
        try:
            self.like = Liked.objects.get(post_id_id = self.id ,user= self.user)
        except:
            self.like = None
        if self.like and self.like.isLike :
            return True
        return False
    def likePost(self):
        if not self.like:
            like = Liked(
                post_id_id= self.id,
                user= self.user
            )
            like.save()
        else :
            self.like.isLike = True
            self.like.save()
        self.post.post_likes += 1
        self.post.save()
    def unlikePost(self):
        if not self.isLike:
            raise "bug"
        self.like.isLike = False
        self.post.post_likes -= 1
        self.like.save()
        self.post.save()
    def getPostDetail(self):
        post = self.post
        #post_serializer = PostSerializer(post, many=True)
        post_author = UserController(post.post_author)
        post_data = {
            self.AUTHOR : post_author.getUserSchool(),
            self.AUTSEX : post_author.getUserSex(),
            self.LIKE : post.post_likes,
            self.TEXT : post.post_text,
            self.TITLE : post.post_title,
            self.CR_DATE : post.created_date,
            self.BOARD_NA:post.board_id.board_name,
            self.P_ID:post.post_id ,
            self.ISLIKE:self.isLike,
            self.COM_COUNT:post.getCommitCount(),
            self.IS_AUT : self.isAuthor,
        }
        
        return post_data
    def getTopCommit(self):
        return Commit.objects.filter(post_id_id = self.id,isDelete=False,likes__gte = 10).order_by('-likes')[:3]
    def getAllCommit(self):
        return Commit.objects.filter(post_id_id = self.id).order_by('created_date')
    def getAllCommitDetail(self,com_list):
        comdel_list = []
        for commit in com_list:
            commit_detail = CommitController(commit,self.user)
            if commit.isDelete:
                data = {
                    self.IS_D:commit.isDelete
                }
            else:
                data = {
                    self.AUTHOR : commit_detail.getAuthorSchool(),
                    self.AUTSEX : commit_detail.getAuthorSex(),
                    self.LIKE : commit.likes,
                    self.TEXT : commit.text,
                    self.CR_DATE : commit.created_date,
                    self.C_ID:commit.id ,
                    self.ISLIKE:commit_detail.isLike,  
                    self.IS_D:commit.isDelete,
                    self.IS_AUT:commit_detail.isAuthor,
                }
            comdel_list.append(data)
        return comdel_list
    def getPostWithTopCommit(self):
        post_data = self.getPostDetail()
        top_commit = self.getTopCommit()
        commit_data = self.getAllCommitDetail(top_commit)
        data = {
            self.POST:post_data,
            self.TOPCOMMIT:commit_data,
        }
        return data
    def getPostOnly(self):
        post_data = self.getPostDetail()
        data = {
            self.POST:post_data,
        }
        return data
    def getOnePost(self):
        post_data = self.getPostDetail()
        all_commit = self.getAllCommit()
        all_commit_data = self.getAllCommitDetail(all_commit)
        top_commit = self.getTopCommit()
        top_commit_data = self.getAllCommitDetail(top_commit)
        data = {
            self.POST:post_data,
            self.COMMIT:all_commit_data,
            self.TOPCOMMIT:top_commit_data,
        }
        return data
    def AreUAuthor(self):
        if self.isUser and self.user == self.post.post_author:
            return True
        else:
            return False
    def editPost(self,new_title,new_text):
        self.post.post_title = new_title
        self.post.post_text = new_text
        self.post.save()
    def delPost(self):
        self.post.isDelete = True
        self.post.save()
class CommitController():
    def __init__(self,commit,user):
        if type(commit) == str:
            commit = Commit.objects.get(pk=commit)
        self.id = commit.id
        self.commit = commit
        self.user = user
        self.author = UserController(self.commit.author)
        self.isUser = user.is_authenticated
        self.isAuthor = False

        if self.isUser :
            self.isLike = self.isLikeorNot()
            if self.commit.author == self.user:
                self.isAuthor = True
        else:
            self.isLike = False
    def AreUAuthor(self):
        if self.isUser and self.user == self.commit.author:
            return True
        else:
            return False
    def editCommit(self,new_text):
        self.commit.text = new_text
        self.commit.save()
    def delCommit(self):
        self.commit.isDelete = True
        self.commit.save()
    def getAuthorSchool(self):
        return self.author.getUserSchool()
    def getAuthorSex(self):
        return self.author.getUserSex()
    def isLikeorNot(self):
        try:
            self.like = CommitLiked.objects.get(commit_id_id = self.id ,user= self.user)
        except:
            self.like = None
        if self.like and self.like.isLike :
            return True
        return False
    def likeCommit(self):
        if not self.like:
            like = CommitLiked(
                commit_id_id= self.id,
                user= self.user
            )
            like.save()
        else :
            self.like.isLike = True
            self.like.save()
        self.commit.likes += 1
        self.commit.save()
    def unlikeCommit(self):
        if not self.isLike:
            raise "bug"
        self.like.isLike = False
        self.commit.likes -= 1
        self.like.save()
        self.commit.save()