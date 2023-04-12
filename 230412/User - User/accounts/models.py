from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 내가 팔로우 한다고 해서 너도 팔로우 할 필요는 없기 때문에 symmetrical=False
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')