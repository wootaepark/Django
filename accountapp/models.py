from django.db import models

# Create your models here.


class HelloWorld(models.Model):  # models.Model을 상속받는다.
    text=models.CharField(max_length=255, null=False)