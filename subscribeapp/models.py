from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscription')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='subscription')

    #user와 project를 연결 시켜준다. user와 user project쌍이 가지는 구독정보는 하나여야 한다. 아래 Meta에 구현

    class Meta:
        unique_together = ('user','project')
