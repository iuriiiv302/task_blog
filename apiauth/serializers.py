from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blogg.models import Post, Voting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('name_post', 'text', 'time_created', 'author_post')


class VotingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voting
        fields = ('vote', 'post', 'user')
