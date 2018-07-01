from django.conf.urls import url
from content import views

urlpatterns = [
    url(r'^prompts/$', views.PromptList.as_view(), name=views.PromptList.name),
    url(r'^prompts/(?P<pk>[0-9]+)$', views.PromptDetail.as_view(), name=views.PromptDetail.name),
    url(r'^artists/$', views.ArtistList.as_view(), name=views.ArtistList.name),
    url(r'^artists/(?P<pk>[0-9]+)$', views.ArtistDetail.as_view(), name=views.ArtistDetail.name),
    url(r'^keyphrases/$', views.KeyphraseList.as_view(), name=views.KeyphraseList.name),
    url(r'^keyphrases/(?P<pk>[0-9]+)$', views.KeyphraseDetail.as_view(), name=views.KeyphraseDetail.name),
    url(r'^subprompt', views.random_subprompt, name='random_subprompt'),
]