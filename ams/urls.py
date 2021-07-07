
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView
from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^menschen/$', TemplateView.as_view(template_name="demands/menschen.html")),

    path('captcha/', include('captcha.urls')),

    path('', include('ams.modules.petition.urls')),
    path('', include('ams.modules.request.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
    ]
