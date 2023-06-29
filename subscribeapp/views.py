from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})
        #project_pk를 GET방식으로 받아서 이 pk를 가지고 있는 detail 페이지로 되돌아 가는 것이다.

    def get(self, request, *args, **kwargs):

        project=get_object_or_404(Project,pk=self.request.GET.get('project_pk'))
        #단축함수를 이용, project_pk를 가지고 있는 Project를 찾는데 그게 만약에 없으면 404메시지로 반응

        user=self.request.user

        #project와 user 두가지 정보를 가지고 subscription을 찾는 것이 아래 코드이다.

        subscription = Subscription.objects.filter(user=user,project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user,project=project).save()
            #구독 정보가 없는 경우 앞서 받은 user,project를 취합해 저장한다.
        return super(SubscriptionView,self).get(request,*args,**kwargs)
