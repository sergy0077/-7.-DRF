from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from django.conf import settings

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
# app = Celery('config', broker='redis://localhost:6379//')
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

# Автоматическое обнаружение и регистрация задач из файлов tasks_old.py в приложениях Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


