
from django.http import HttpResponseForbidden


from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args,**kwargs):  #일반 get,post 함수(메소드)와 구조가 동일하다고 생각만 하자
        comment = Comment.objects.get(pk=kwargs['pk'])
        # 장고 기본 유저를 가져와서, 요청을 받으면서 primarykey로 받은 그 값을 가지고 있는 유저 object가 user가 되는 것이다.

        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated

# get,post 든 뭐든 간에 받을 때 마다 그 pk를 확인해서 그 user object가 실제로 request를 보낸 user와 같은지 아닌지 확인 후
# 아니면  에러 페이지 전송, 일치 하는 경우 그 함수 그대로 보냄