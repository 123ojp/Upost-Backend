from users.models import *

from rest_framework import serializers

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'groups']




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
