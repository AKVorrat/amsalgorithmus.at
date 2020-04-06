
from django.conf import settings
from django.views.static import serve
from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', include('ams.modules.petition.urls')),
    path('', include('ams.modules.request.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]
