from poster.models import *

from rest_framework import serializers

#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'groups']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text','created_date','post_id','post_likes']
        
class CommitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [ 'post_id','likes','text']




class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['board_id', 'board_name','isSchoolBoard']

class CommitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['post_id', 'likes','text']