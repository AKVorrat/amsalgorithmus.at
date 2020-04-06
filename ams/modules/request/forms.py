from django import forms

class RequestForm(forms.Form):
    first_name = forms.CharField(
        label="Vorname",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )
    last_name = forms.CharField(
        label="Nachname",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )

    email = forms.EmailField(
        label="E-Mail Adresse",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )

    address = forms.CharField(
        label="Adresse",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )

    zipcode = forms.CharField(
        label="PLZ",
        max_length=4,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )

    municipality = forms.CharField(
        label="Ort",
        max_length=255,
        widget=forms.TextInput(attrs={'class': "request-input"})
    )

    @property
    def full_name(self):
        return '{0} {1}'.format(self.cleaned_data['first_name'], self.cleaned_data['last_name'])
