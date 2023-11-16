from rest_framework import serializers
from habits.models import Habit
from habits.validators import HabitValidator, HabitTimeValidator
from .validators import LimitHabits, LimitTime, Limitdays, RelatedHabitorReward


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitValidator(field1='related_habit', field2='is_pleasant'),
            HabitTimeValidator(fields='time'),
            LimitTime(field_name='time_complete', max_seconds=120),
            RelatedHabitorReward(related_field='related_Habit', reward_field='reward'),
            Limitdays(field_name='periodicity', max_days=7),
            LimitHabits(field_name_1='sign_of_a_pleasant_habit', field_name_2='reward', field_name_3='related_Habit')
        ]



