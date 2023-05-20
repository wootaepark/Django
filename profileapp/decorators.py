
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args,**kwargs):  #일반 get,post 함수(메소드)와 구조가 동일하다고 생각만 하자
        profile = Profile.objects.get(pk=kwargs['pk'])


        if not profile.user == request.user: #이 profile을 보내는 유저와 request를 보내는 유저가 같지 않다면
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
# get,post 든 뭐든 간에 받을 때 마다 그 pk를 확인해서 그 user object가 실제로 request를 보낸 user와 같은지 아닌지 확인 후
# 아니면  에러 페이지 전송, 일치 하는 경우 그 함수 그대로 보냄