from django.utils import timezone
from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""
    PERIOD_CHOICES = (
        ('DAILY', 'каждый день'),
        ('WEEKLY', 'раз в неделю')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name='Создатель привычки', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='место, в котором нужно выполнять прывычку')
    time = models.TimeField(verbose_name='Время, когда необходимо выполнять привычку')
    habit_action = models.CharField(max_length=255, default='default_value', verbose_name='действие, которое представляет из себя привычка')

    is_pleasant = models.BooleanField(verbose_name='Признак приятной привычки', default=False)
    related_Habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)

    period = models.CharField(max_length=15, verbose_name='Периодичность выполнения привычки для напоминания в днях', choices=PERIOD_CHOICES, default='DAILY')
    reward = models.TextField(verbose_name='Вознаграждение, которым пользователь должен себя вознаградить после выполнения', **NULLABLE)

    time_to_complete = models.DurationField(verbose_name='Время на выполнение пользователем привычки в секундах', default=timezone.timedelta(minutes=2))
    is_public = models.BooleanField(verbose_name='Признак публичности привычки (в общем доступе)', default=False)

    objects = models.Manager()

    def should_be_done_today(self):
        """
        Проверяет, должна ли привычка быть выполнена сегодня.
        """
        current_day = timezone.now().weekday()
        # Получаем текущий день недели (0-6, где 0 - понедельник, 6 - воскресенье)
        # Проверяем, если привычка ежедневная или если текущий день совпадает с днем, когда привычка должна быть выполнена
        if self.period == 'DAILY' or (self.period == 'WEEKLY' and current_day == self.day_of_week()):
            return True
        return False

    def day_of_week(self):
        # Предполагаем, что self.period содержит 'DAILY' для ежедневной привычки и 'WEEKLY' для еженедельной
        if self.period == 'WEEKLY':
            # Если привычка еженедельная, предполагаем, что self.day_of_week содержит числовое значение дня недели
            # от 0 (понедельник) до 6 (воскресенье). Возвращаем это значение.
            return self.day_of_week
        else:
            # Если привычка ежедневная, всегда возвращаем текущий день недели.
            # Для воскресенья вернется 6, для понедельника вернется 0 и так далее.
            return timezone.now().weekday()

    def __str__(self):
        return f"я буду {self.habit_action} в {self.time} в {self.place}\nВремя на выполнение: {self.time_to_complete}\n"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('owner',)