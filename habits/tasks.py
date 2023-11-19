import os
import requests
from celery import shared_task
from habits.models import Habit


@shared_task
def create_periodic_tasks(*args, **kwargs):
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHANNEL_ID')

    habits = Habit.objects.all()

    for habit in habits:
        action = habit.habit_action
        time = habit.time
        place = habit.place
        reward = habit.reward

        def get_reward_or_habit():
            if reward:
                return reward
            else:
                return None

        text = f'я буду {action} в {time} в {place}. После этого {get_reward_or_habit()}'
        params = {'chat_id': chat_id, 'text': text}
        data = requests.get(f'https://api.telegram.org/bot{bot_token}/sendMessage', params=params).json()
        print(data)

