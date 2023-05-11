from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    # 여기 까지는 AccountUpdateForm 과 UserCreationForm 은 같은 기능을 한다고 할 수 있다.

        self.fields['username'].disabled = True
        # 이 구문이 추가됨으로서 username의 칸을 비활성화 시켜주는 코드이다.
        # 원치 않게 username을 변경하였다 하더라도 True인 이상 서버에 그 값이 반영되지는 않는다.