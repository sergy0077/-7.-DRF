# Generated by Django 4.2.6 on 2023-10-26 23:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('action', models.CharField(max_length=255)),
                ('is_rewarding', models.BooleanField(default=False)),
                ('frequency_days', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('reward', models.CharField(blank=True, max_length=255, null=True)),
                ('execution_time_minutes', models.IntegerField(validators=[django.core.validators.MaxValueValidator(120)])),
                ('is_public', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('telegram_chat_id', models.CharField(blank=True, max_length=255, null=True)),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HabitLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_date', models.DateField(auto_now_add=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
