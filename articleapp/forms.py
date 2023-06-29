from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model=Article
        fields=['title','image','project','content']


#  이전에 Profiileapp에서 했던 것과 마찬가지로 적용할 필드 설정과, 우리가 만든 모델인 Article을 가져와서 UserCreationFrom을 생성