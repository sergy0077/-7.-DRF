import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from habits.models import Habit
from datetime import datetime, date

habit = Habit.objects.all()

for h in habit:
    periods = h.period
    time = h.time


def periods():
    if periods == 'DAILY':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.DAYS,
        )
        return schedule
    elif periods == 'WEEKLY':
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=7,
            period=IntervalSchedule.DAYS,
        )
        return schedule


def create_schedule():
    return PeriodicTask.objects.create(
        interval=periods(),
        name='Habit reminder',
        task='habits.tasks.create_periodic_tasks',
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({'arg1': 'arg2'}),
        start_time=datetime.combine(date.today(), time),
    )
