from django.contrib import admin
from django.http import HttpResponse
from .models import Signature

class SignatureAdmin(admin.ModelAdmin):
    actions = ['resend_email']

    def resend_email(self, request, queryset):
        for signature in queryset:
            if not signature.confirmed:
                signature.send_confirmation_email(request)
        return HttpResponse('OK')

    resend_email.short_description = "Bestätigungsmail erneut senden"

admin.site.register(Signature, SignatureAdmin)
