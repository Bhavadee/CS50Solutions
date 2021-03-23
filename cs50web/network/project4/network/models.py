from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "writer_name": self.user.username,
            "writer_id": self.user.id,
            "content": self.content,
            "likes": self.likes,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p"),
        }

class Profile(models.Model):
    followed_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following_me")
    follower_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="me_following")  