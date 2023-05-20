from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model=Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name='profileapp/create.html'

    def form_valid(self, form): #form은 우리가 보는 form (forms.py에 있는 Form 클래스) 데이터
        temp_profile = form.save(commit=False) # 실제 DB에 저장하지 않고 임시로 저장, commit = False를 하여 임시데이터가 저장되게 된다.
        temp_profile.user = self.request.user # 임시 객체의 user는 self에서 request를 보낸 당사자 user로 정해준다. (나 자신)
        temp_profile.save() # 그리고 최종적으로 저장
        return super().form_valid(form) # 나머지는 위의 ProfileCreateView 안에 있는 원래 결과를 리턴

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model=Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name='profileapp/update.html'




