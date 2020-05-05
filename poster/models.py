from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)
# Create your models here.
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    board_name = models.CharField(max_length=200)
    isSchoolBoard = models.BooleanField(default=False)
    school_id = models.ForeignKey('schools.School',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    def __str__(self):
        return self.board_name
    def getName(self):
        if self.isSchoolBoard == True:
            return self.school_id.school_name
        else:
            return self.board_name

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    post_id = models.AutoField(primary_key=True)
    post_author = models.ForeignKey(User,
        on_delete=models.CASCADE)#使用者刪除 文章消失
    isDelete = models.BooleanField(default=False)#軟刪除
    board_id = models.ForeignKey(Board,
        on_delete=models.CASCADE,
        default = None)
    #published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()
    def __str__(self):
        return self.post_title
    def getCommitCount(self):
        return Commit.objects.filter(post_id=self).count()

class Commit(models.Model):
    author = models.ForeignKey(User,
        on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,
        on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    isDelete = models.BooleanField(default=False)#軟刪除
    def __str__(self):
        return str(self.post_id.post_title) + ' - ' + self.text

class Liked(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,
        on_delete=models.CASCADE)
    isLike = models.BooleanField(default=True)#軟刪除
    def __str__(self):
        return str(self.post_id) + ' - ' + str(self.user)
    
class CommitLiked(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    commit_id = models.ForeignKey(Commit,
        on_delete=models.CASCADE)
    isLike = models.BooleanField(default=True)#軟刪除
    def __str__(self):
        return str(self.commit_id) + ' - ' + str(self.user)