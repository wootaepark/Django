from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"
# 주소 접근을 쉽게 하기 위한 app_name 불필요하게 중복 해주는 것이 아니다. 아래처럼 나중에 활용 가능
"accountapp:hello_world"

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Login 뷰와 Logout 뷰는 장고에서 제공해준다.

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    #pk 라는 이름의 int 정보를 받겠다 라는 의미
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),


]
