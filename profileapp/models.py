from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    # 장고에서 제공해주는 필드중 하나 Profile과 user 객체를 하나씩 연결해 주는 역할

    #on_delete 는 연결되어있는 User 객체가 delete 될때 그와 연결되어 있는 Profile객체가 어떤 행동을 보일 것인지에 대한 정책을 담당
    #이 객체가 사라 질때 CASECADE 즉 이 Profile도 없어지게 설정하는 것이다.
    #즉 User가 탈퇴하면 이 Profile도 사라진다는 의미로 받아들이자.
    #related_name 은 request.user.profile과 같이 따로 Profile 객체를 찾지 않더라도 이 객체의 profile 에 바로 연결할 수 있게
    #이름을 정해주는 것이다.  nickname 필드가 있으면 request.user.profiie.nickname 처럼 접근 할 수도 있다.
    

    image = models.ImageField(upload_to='profile/',null=True)
    # upload_to 는 우리가 이미지를 받으면 이미지 파일을 서버 내부에 저장을 할 것인데, 그 이미지의 저장 경로를 정해준다.
    # 우리가 전에 설정해준 media/ 하위에 profile 이라는 경로가 추가 되서 그안에 들어갈 것이다.
    # null=True는 프로필 사진을 올리지 않아도 괜찮다는 의미로서 동작한다.

    nickname = models.CharField(max_length=20,unique=True, null=True)
    # 최대 길이는 20으로 지정하고 unique=True 를 통해 이 profile객체에서 이 nickname은 하나가 유일해야한다는 의미

    message = models.CharField(max_length=100,null=True)