from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from blogg.models import Post, Voting
from .serializers import UserSerializer, GroupSerializer, PostSerializer, VotingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class VotingViewSet(viewsets.ModelViewSet):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
