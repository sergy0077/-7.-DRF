from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitListPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner
from users.models import User
from habits.tasks import create_periodic_tasks


class CreateHabitAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class UpdateHabitAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class ListHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]
    pagination_class = HabitListPaginator


class ListPublicHabitAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitListPaginator

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)


class RetrieveHabitAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class DestroyHabitAPIView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


def SendMessageView(request, user_id, chat_id):
    user = User.objects.get(id=user_id)

    if not user_id or not chat_id:
        return HttpResponse("error: user_id or chat_id is missing")

    text = f"Здравствуйте {user.first_name}, пришло время выполнять привычки."
    create_periodic_tasks.delay(chat_id=chat_id, message=text)
    return HttpResponse('Message sent successfully.')
