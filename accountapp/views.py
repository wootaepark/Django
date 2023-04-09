from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST": # 요청을 받은 객체 내에서 메소드를 찾는데 이것이 POST 메소드 일 경우

        # request의 POST 중에서 hello_world_input 이라는 이름을 가진 데이터를 temp 에 대입.
        temp=request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
         # context == 데이터 꾸러미, text라는 이름으로 전달,  temp 데이터 꾸러미를 넣어서 리턴한다는 뜻



    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})

