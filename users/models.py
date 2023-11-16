from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, verbose_name="Имя пользователя(как в TG)")
    email = models.EmailField(max_length=60, unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, verbose_name='имя', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='фамилия', blank=True, null=True)
    surname = models.CharField(max_length=200, verbose_name='отчествоо', **NULLABLE)
    telegram_chat_id = models.CharField(max_length=255, blank=True, null=True,
                                        verbose_name='Поле для хранения идентификатора чата в Telegram')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'



