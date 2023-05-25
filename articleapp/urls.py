from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(template_name='articleapp/list.html'),name='list'),



    path('create/', ArticleCreateView.as_view(),name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(),name='detail'),

    # 몇번 article 로 가야 하는지 알려줘야 하기 때문에 <int:pk> 삽입
    path('update/<int:pk>', ArticleUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(),name='delete'),
]