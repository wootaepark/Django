from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership=[account_ownership_required, login_required] # decorator들의 배열 생성 (아래에서 처럼 간략화 하기 위함)


class AccountCreateView(CreateView): #CreateView를 상속 받는 클래스
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'
    # CreateView는 뭔가를 만들어야 되니까 form 이랑 성공시 리다이렉트 할 주소를 정해준 반면
    # DetailView는 어떤 모델을 쓰고 모델 내부의 정보를 어떻게 시각화 할지를 신경을 써줘면 된다.

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView,self).get_context_data(object_list=object_list,**kwargs)



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
