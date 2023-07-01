from django.forms import ModelForm
from django import forms # forms를 가져옴, 대문자는 잘가져 오는데 소문자는 잘 가져오지 못하는 경향이 있다.

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    content = forms.CharField(widget = forms.Textarea(attrs={'class':'editable text-left',
                                                             'style': 'height : auto;'}))


    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    class Meta:
        model = Article
        fields=['title','image','project','content']


#  이전에 Profiileapp에서 했던 것과 마찬가지로 적용할 필드 설정과, 우리가 만든 모델인 Article을 가져와서 UserCreationFrom을 생성