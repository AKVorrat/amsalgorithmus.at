from django import forms
from django.utils.translation import gettext_lazy as _

class RequestForm(forms.Form):
    required_css_class = 'required'

    first_name = forms.CharField(
        label=_("Vorname"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )
    last_name = forms.CharField(
        label=_("Nachname"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    email = forms.EmailField(
        label=_("E-Mail-Adresse"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    address = forms.CharField(
        label=_("Adresse"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    zipcode = forms.CharField(
        label=_("PLZ"),
        max_length=4,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    municipality = forms.CharField(
        label=_("Ort"),
        max_length=255,
        widget=forms.TextInput(attrs={'class': "form-input"})
    )

    @property
    def full_name(self):
        return '{0} {1}'.format(self.cleaned_data['first_name'], self.cleaned_data['last_name'])
