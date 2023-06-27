from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/combinationdata', views.CombinationdataViewSet.as_view(), name='core_combinationdata'),
    path('api/pollsquestion', views.PollsQuestionViewSet.as_view(), name='core_pollsquestion'),
]