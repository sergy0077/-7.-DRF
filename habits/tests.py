from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_username',
            email='test@mail.ru',
            is_active=True
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.user.set_password('qwe123rty456')
        self.user.save()
        self.habit_data = {
            'place': 'Home',
            'habit_action': 'Drink water',
            'reward': 'eat apple',
            'time_to_complete': timezone.timedelta(minutes=2),
            'time': timezone.now()
        }
        self.habit = Habit.objects.create(**self.habit_data)

    def test_create_habit(self):
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': self.habit.reward,
            'time_to_complete': str(self.habit.time_to_complete),
            'time': '00:02:00'
        }
        response = self.client.post(
            reverse('habits:create-habit'),
            data=data, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_list_habit(self):
        response = self.client.get(reverse('habits:list-habit'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        User.objects.all().delete()
        Habit.objects.all().delete()

    def test_create_habit_err1(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "You haven't filled in one of these fields. Please, fill in one of the two (nice_habit/reward) fields"
                             ]
                         }
                         )

    def test_create_habit_err2(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': 'Eat sweet',
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Please, fill in one of the two (nice_habit/reward) fields"
                             ]
                         }
                         )

    def test_create_habit_err3(self):
        """Тест для проверки валидатора"""
        data = {
            'place': self.habit.place,
            'habit_action': self.habit.habit_action,
            'reward': 'Eat sweet',
            'time_to_complete': "00:25:00"
        }
        response = self.client.post(reverse('habit:create-habit'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(),
                         {
                             "non_field_errors": [
                                 "Please, write correct time. Time must be less than 120 seconds"
                             ]
                         }
                         )