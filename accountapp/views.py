from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST": # 요청을 받은 객체 내에서 메소드를 찾는데 이것이 POST 메소드 일 경우

        # request의 POST 중에서 hello_world_input 이라는 이름을 가진 데이터를 temp 에 대입.
        temp=request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()  #DB 연결을 하겠다는 것
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()  #HelloWorld의 모든 데이터를 다 가져온다는 뜻, hello_world_list에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        #accountapp에 있는 hello_world로 재접속하라는 response를 보내주게 된다.
        #render를 쓰면 계속 반복됨 (get으로 호출이 되지 않는다.)

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # context == 데이터 꾸러미, text라는 이름으로 전달,  temp 데이터 꾸러미를 넣어서 리턴한다는 뜻


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

class AccountUpdateView(UpdateView):
    model = User
    #form_class = UserCreationForm
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
