from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.conf import settings
from .forms import SignatureForm, WithdrawalForm
from .models import Signature
from math import log10, trunc

class PetitionView(FormView):
    template_name = 'index.html'
    form_class = SignatureForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        count = Signature.objects.filter(confirmed=True).count()
        if count >= 100:
            goal = 10**(trunc(log10(count)) + 1)
            if count < goal//2:
                goal //= 2
        else:
            goal = 100
        kwargs['signature_count'] = count 
        kwargs['goal'] = goal
        kwargs['progress'] = str((kwargs['signature_count'] / kwargs['goal']) * 100).replace(',', '.')
        kwargs['locale'] = settings.LOCALE_PATHS
        return super(PetitionView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if form.pending_signature:
                if form.pending_signature.emails_sent < 5:
                    form.pending_signature.send_confirmation_email(request)
            elif form.confirmed_signature:
                if form.confirmed_signature.emails_sent < 5:
                    form.confirmed_signature.send_already_confirmed_email(request)
            else:
                form.instance.send_confirmation_email(request)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
            
class ConfirmEmailView(TemplateView):
    template_name = 'confirm.html'

    def get(self, request, *args, token=None, **kwargs):
        try:
            signature = Signature.objects.get(token=token)
        except Signature.DoesNotExist:
            return super().get(request, *args, confirmed=False, **kwargs)
        signature.confirm(token)
        return super().get(request, *args, confirmed=signature.confirmed, **kwargs)

class PrivacyView(FormView):
    template_name = 'privacy.html'
    form_class = WithdrawalForm
    success_url = '/privacy/withdrawal'
    fail_url = '/privacy/#withdrawal'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            if form.signature:
                form.signature.send_withdrawal_email(request)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ConfirmWithdrawalView(TemplateView):
    template_name = 'withdraw.html'

    def get(self, request, *args, token=None, **kwargs):
        try:
            signature = Signature.objects.get(withdrawal_token=token)
        except Signature.DoesNotExist:
            return super().get(request, *args, withdrawn=False, **kwargs)
        signature.withdraw(token)
        return super().get(request, *args, withdrawn=True, **kwargs)

