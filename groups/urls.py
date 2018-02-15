from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from groups import views


urlpatterns = [
    url(r'^groups/$', views.GroupList.as_view(), name='groups-list'),
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupDetail.as_view(), name='groups-detail'),
    url(r'^elements/$', views.ElementList.as_view(), name='elements-list'),
    url(r'^elements/(?P<pk>[0-9]+)/$', views.ElementDetail.as_view(), name='elements-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)