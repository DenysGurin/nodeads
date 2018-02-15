"""nodeads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin

from django.conf.urls import url, include
from django.conf.urls.static import static

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.documentation import include_docs_urls


@api_view(['GET'])
def api_root(request, format=None):
    """
    get:
    Return a list of all endpoints.
    """
    return Response({
        'groups/': reverse('groups-list', request=request, format=format),
        'elements/': reverse('elements-list', request=request, format=format),
    })


urlpatterns = [
    url(r'^$', api_root),
    url('admin/', admin.site.urls),
    url(r'^', include('groups.urls')),
    url(r'^docs/', include_docs_urls(title='NodeAds test task', 
                                     public=False))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)