from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink


class Post(models.Model):
    name_post = models.TextField()
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')


class Voting(models.Model):
    vote = models.IntegerField(default=-0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='voting_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='voting_user')





