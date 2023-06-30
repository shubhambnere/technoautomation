from django.urls import path,include
from core.views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import site
from django.views.static import serve
from django.urls import re_path


urlpatterns = [

    path('admin/', site.urls),
    path('', include('core.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]



urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)