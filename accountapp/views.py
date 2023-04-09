from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):

    if request.method == "POST": # 요청을 받은 객체 내에서 메소드를 찾는데 이것이 POST 메소드 일 경우
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'})
    # context == 데이터 꾸러미, text라는 이름의 POST method!!! 라는 내용을 가진 데이터 꾸러미를 넣어서 리턴한다는 뜻
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})

