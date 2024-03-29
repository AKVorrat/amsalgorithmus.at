from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.utils.translation import gettext as _
from urllib.parse import urlparse
from .tokens import TokenGenerator

generator = TokenGenerator()

class Signature(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(_("E-Mail"), max_length=255, unique=True)
    token = models.CharField(max_length=24, unique=True)
    emails_sent = models.IntegerField(default=0)
    withdrawal_emails_sent = models.IntegerField(default=0)
    withdrawal_token = models.CharField(max_length=24, null=True, blank=True)

    confirmed = models.BooleanField(default=False)
    newsletter = models.BooleanField()

    class Meta:
        verbose_name = "Unterschrift"
        verbose_name_plural = "Unterschriften"

    def __str__(self):
        return '[{}] {} {}, {}'.format(
            'Confirmed' if self.confirmed else 'Pending',
            self.first_name, self.last_name, self.email 
        )
    
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def validate_unique(self, exclude=None):
        exclude = ['email'] if not exclude else exclude + ['email']
        super(Signature, self).validate_unique(exclude=exclude)

    def send_confirmation_email(self, request):
        if not self.token:
            self.token = generator.make_token(self)
            self.save()
        confirmation_url = '/confirm/{}/'.format(self.token)
        confirmation_url = request.build_absolute_uri(confirmation_url)

        context = {
            'confirmation_url': confirmation_url,
            'full_name': self.full_name(),
            'wants_newsletter': self.newsletter
        }
        send_mail(
            _('[amsalgorithmus.at] Bitte bestätige deine E-Mail-Adresse.'),
            render_to_string('email/confirm.txt', context),
            'noreply@epicenter.works',
            [self.email],
            html_message=render_to_string('email/confirm.html', context),
            fail_silently=False
        )
        self.emails_sent += 1
        self.save()

    def send_already_confirmed_email(self, request):
        context = {
            'full_name': self.full_name()
        }
        send_mail(
            '[amsalgorithmus.at] Du hast bereits an der Petition teilgenommen.',
            render_to_string('email/already_confirmed.txt', context),
            'noreply@epicenter.works',
            [self.email],
            html_message=render_to_string('email/already_confirmed.html', context),
            fail_silently=False
        )
        self.emails_sent += 1
        self.save()


    def confirm(self, token):
        if generator.check_token(self, token):
            self.confirmed = True
            self.emails_sent = 0
            self.save()
            if self.newsletter and hasattr(settings, 'DIALOGMAIL_SECRET'):
                from .dialogmail import dialogmail_subscribe
                from dialogmail import DialogMailError
                try:
                    dialogmail_subscribe(self.email)
                except DialogMailError:
                    pass

    def send_withdrawal_email(self, request):
        if not self.withdrawal_token:
            self.withdrawal_token = generator.make_token(self)
            self.save()
        withdrawal_url = '/withdraw/{}/'.format(self.withdrawal_token)
        withdrawal_url = request.build_absolute_uri(withdrawal_url)

        context = {
            'withdrawal_url': withdrawal_url,
            'full_name': self.full_name(),
            'has_newsletter': self.newsletter
        }
        send_mail(
            '[amsalgorithmus.at] Bitte bestätige deinen Widerruf.',
            render_to_string('email/withdraw.txt', context),
            'noreply@epicenter.works',
            [self.email],
            html_message=render_to_string('email/withdraw.html', context),
            fail_silently=False
        )
        self.withdrawal_emails_sent += 1
        self.save()

    def withdraw(self, token):
        if generator.check_token(self, token):
            if self.newsletter and hasattr(settings, 'DIALOGMAIL_SECRET'):
                from .dialogmail import dialogmail_unsubscribe
                from dialogmail import DialogMailError
                try:
                    dialogmail_unsubscribe(self.email)
                except DialogMailError:
                    pass
            self.delete()

