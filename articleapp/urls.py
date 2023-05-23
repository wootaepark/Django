from django.urls import path
from django.views.generic import TemplateView



app_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'),name='list'),
    # TemplateView는 장고에서 기본 제공해주는 view인데, articleapp의 list.html을 이용할 것이다.

]