from django.db import models

# Create your models here.

class Project(models.Model):
    image=models.ImageField(upload_to='project/', null=False)
    title=models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.pk} : {self.title}' #몇번 게시판의 이름을 리턴한다. f를 이용하면 특정 변수를 출력 시킬 수 있게 됨