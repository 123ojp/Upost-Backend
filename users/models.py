from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

#for user in User.objects.all():
#    Token.objects.get_or_create(user=user)
# Create your models here.


class UnverifyUser(models.Model):
    username = models.CharField(unique=True,max_length=30)
    email = models.EmailField()
    token = models.CharField(unique=True,max_length=40)
    isCreate = models.BooleanField(default=False)
    school = models.ForeignKey('schools.School',
        on_delete=models.CASCADE,
        default = None )
    def __str__(self):
        return self.username




class UserDetail(models.Model):
    user = models.OneToOneField(User,
            on_delete=models.CASCADE, related_name='profile')
    school = models.ForeignKey('schools.School',
        on_delete=models.CASCADE)
    sex = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user)
