import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('EMAIL_HOST_USER'),
            first_name=os.getenv('EMAIL_FIRST_NAME'),
            last_name=os.getenv('EMAIL_LAST_NAME'),
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        user.set_password(os.getenv('EMAIL_HOST_PASSWORD'))
        user.save()