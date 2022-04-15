from django import forms, template
from django.utils.functional import lazy
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from captcha.fields import CaptchaField
from .models import Signature


mark_safe_lazy = lazy(mark_safe, str)


class SignatureForm(forms.ModelForm):
    auto_id = False
    required_css_class = 'required'
    first_name = forms.CharField(
        label=_("Vorname"),
        label_suffix = "",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '})
    )
    last_name = forms.CharField(
        label=_("Nachname"),
        label_suffix = "",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '})
    )

    email = forms.EmailField(
        label=_("E-Mail-Adresse"),
        label_suffix = "",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input", 'placeholder': ' '})
    )

    captcha = CaptchaField()

    newsletter = forms.BooleanField(
        initial=False,
        required=False,
        label=mark_safe_lazy(_('Ja, ich will den <a target="_blank" href="https://epicenter.works/newsletter">Newsletter</a> erhalten (optional).')),
        label_suffix = ""
    )
    privacy_policy = forms.BooleanField(
        initial=False,
        required=True,
        label=mark_safe_lazy(_('Ja, ich stimme den <a target="_blank" href="/privacy">Datenschutzbedingungen</a> zu.')),
        label_suffix = ""
    )

    def clean(self):
        super(SignatureForm, self).clean()
        email = self.cleaned_data.get('email')
        self.pending_signature = None
        self.confirmed_signature = None
        try:
            s = Signature.objects.get(email=email)
        except Signature.DoesNotExist:
            return

        if not s.confirmed:
            self.pending_signature = s
        else:
            self.confirmed_signature = s

    class Meta:
        auto_id = False
        model = Signature
        fields = ['first_name', 'last_name', 'email', 'newsletter']

class WithdrawalForm(forms.Form):
    email = forms.EmailField(
        label=_("E-Mail-Adresse"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    def clean(self):
        super(WithdrawalForm, self).clean()
        email = self.cleaned_data.get('email')
        self.signature = None
        try:
            self.signature = Signature.objects.get(email=email)
        except Signature.DoesNotExist:
            return
        if self.signature.withdrawal_emails_sent >= 5:
            self.signature = None

