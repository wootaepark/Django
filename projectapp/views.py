from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ProjectCreateView(CreateView):
    model=Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk': self.object.pk})



class ProjectDetailView(DetailView,MultipleObjectMixin):
    model=Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    #아래는 어떤 게시글을 가져올지에 대한 필터링 구문이다.

    def get_context_data(self, **kwargs):
        project=self.object
        user=self.request.user

        #user와 project를 가져온다.

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)
            #subscription 변수에 user와 project정보를 대입한다.

        else:
            subscription = None

        object_list=Article.objects.filter(project=self.get_object())
        #현재프로젝트의 오브젝트를 가진 article 들을 모두 필터링 하는 것이다.
        return super(ProjectDetailView,self).get_context_data(object_list=object_list,
                                                              subscription=subscription,
                                                              **kwargs)
        #템플릿 창에서 object_list라는 것을 사용해서 필터링한 게시글들을 사용할 수 있게 된다.
        #추가적으로 위의 if문에서 찾은 subscription 정보로 subscriptoin을 대체한다.



class ProjectListView(ListView):
    model=Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25



