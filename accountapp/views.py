from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

has_ownership=[account_ownership_required, login_required] # decorator들의 배열 생성 (아래에서 처럼 간략화 하기 위함)
@login_required
def hello_world(request):
    if request.method == "POST":  # 요청을 받은 객체 내에서 메소드를 찾는데 이것이 POST 메소드 일 경우
        # request의 POST 중에서 hello_world_input 이라는 이름을 가진 데이터를 temp 에 대입.

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  # DB 연결을 하겠다는 것
        new_hello_world.text = temp
        new_hello_world.save()
        # hello_world_list = HelloWorld.objects.all()  #HelloWorld의 모든 데이터를 다 가져온다는 뜻, hello_world_list에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # accountapp에 있는 hello_world로 재접속하라는 response를 보내주게 된다.
        # render를 쓰면 계속 반복됨 (get으로 호출이 되지 않는다.)

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # context == 데이터 꾸러미, text라는 이름으로 전달,  temp 데이터 꾸러미를 넣어서 리턴한다는 뜻 , 딕셔너리 형


class AccountCreateView(CreateView): #CreateView를 상속 받는 클래스
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
    # CreateView는 뭔가를 만들어야 되니까 form 이랑 성공시 리다이렉트 할 주소를 정해준 반면
    # DetailView는 어떤 모델을 쓰고 모델 내부의 정보를 어떻게 시각화 할지를 신경을 써줘면 된다.



    """def get(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args,**kwargs)
        else:
            return HttpResponseForbidden()

    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args,**kwargs)
        else:
            return HttpResponseForbidden()"""
        
        # 데코레이터 전의 함수(메소드) get,post이다.



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User #장고에서 기본 제공해주는 유저
    #form_class = UserCreationForm
    form_class = AccountUpdateForm
    context_object_name = 'target_user' # 모델의 별명 (User의 별명)
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'



#@method_decorator(login_required, 'get')
#@method_decorator(login_required, 'post')
#@method_decorator(account_ownership_required, 'get')
#@method_decorator(account_ownership_required, 'post')  이 코드들이 아래오 같이 두줄로 간략화
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    """def get(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args,**kwargs)
        else:
            return HttpResponseForbidden() #금지되어 있는 곳에 접근 했다는 것을 보여줌

    def post(self,*args,**kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args,**kwargs)
        else:
            return HttpResponseForbidden()"""
