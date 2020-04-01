from django.urls import include, path, re_path
from django.views.generic import TemplateView
from .views import PetitionView, ConfirmEmailView, \
                    PrivacyView, ConfirmWithdrawalView

urlpatterns = [ 
    re_path(r'^confirm/(?P<token>.{24})/', ConfirmEmailView.as_view(), name="confirm-email"),
    re_path(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),
    re_path(r'^privacy/$', PrivacyView.as_view()),
    re_path(r'^privacy/withdrawal$', TemplateView.as_view(template_name="withdrawal_sent.html")),
    re_path(r'^withdraw/(?P<token>.{24})/', ConfirmWithdrawalView.as_view()),
    re_path(r'^$', PetitionView.as_view())
]
