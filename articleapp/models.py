from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='article',null=True)
    # on_delete = models.SET_NULL 은 Article이 회원 탈퇴를 했을때 게시글이 사라지지 않고, 알 수 없음으로 주인없는 게시글이 되는걸로 설정한 것
    # article 이라는 이름으로 설정한 이유는 User에서 접근할 때 article이라고 하며 접근하는 것이 자연스럽다고 생각
    # SET_NULL로 설정을 앞에서 해줬기 때문에 null이 가능하도록 True값으로 설정

    title=models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='article/',null=False) #False를 통해 이미지를 항상 넣도록 한다.
    content=models.TextField(null=True) # 좀더 긴 글을 적을 필요가 있으므로 CharField 보다는 TextField를 적용하였다.

    created_at = models.DateField(auto_now_add=True,null=True)
    # 언제 만들어 졌는지에 대한 정보 관련 코드, 자동 생성시에도 값이 저장되도록 하는 auto_created

    # 수정 : auto_new_add 로 변경하였는데 그 이유는 정상적으로 데이터가 쌓이게 되는 것이다.




