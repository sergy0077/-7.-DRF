from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=input('Введите вашу почту '),
            first_name=input('Введите ваше имя '),
            last_name=input('Введите вашу фамилию '),
            is_active=True,
        )
        user.set_password(input('Введите ваш пароль '))
        user.save()