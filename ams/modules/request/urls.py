from django.urls import re_path
from .views import RequestView

urlpatterns = [ 
    re_path(r'^request/$', RequestView.as_view()),
]
