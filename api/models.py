from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userid = models.CharField(max_length=10, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10, unique=True, default="")
    user_image = models.ImageField(blank=True)
    post_num = models.IntegerField(default=0)

    def __str__(self):
        return self.profile.username

class Upload(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="uploads")
    description = models.TextField(blank=True)
    upload_date = models.DateField(auto_now=False, auto_now_add=True)
    like_num = models.IntegerField()
    comment_num = models.IntegerField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.upload.description

