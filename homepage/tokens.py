from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import encoding
from django.core.mail import send_mail
from django.conf import settings

class PasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) +
            str(user.is_active)
        )
account_activation_token = PasswordResetTokenGenerator()
