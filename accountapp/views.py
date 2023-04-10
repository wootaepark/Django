from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST": # 요청을 받은 객체 내에서 메소드를 찾는데 이것이 POST 메소드 일 경우

        # request의 POST 중에서 hello_world_input 이라는 이름을 가진 데이터를 temp 에 대입.
        temp=request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # hello_world_list = HelloWorld.objects.all()  #HelloWorld의 모든 데이터를 다 가져온다는 뜻, hello_world_list에 저장

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        #accountapp에 있는 hello_world로 재접속하라는 response를 보내주게 된다.




    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # context == 데이터 꾸러미, text라는 이름으로 전달,  temp 데이터 꾸러미를 넣어서 리턴한다는 뜻
