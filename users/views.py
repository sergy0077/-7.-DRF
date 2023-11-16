from rest_framework import generics, status
from rest_framework.reverse import reverse
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner


class UserCreationApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            # Генерация URL для создания пользователя и добавление в JSON-ответ
            user_create_url = reverse('users:user_create')
            response.data['user_create_url'] = user_create_url
        return response


class UsersCreateView(generics.CreateAPIView):
    """Контроллер создания пользователя"""
    serializer_class = UserCreateSerializer


class UsersListView(generics.ListAPIView):
    """Контроллер списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]


class UsersDetailView(generics.RetrieveAPIView):
    """Контроллер описания пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersUpdateView(generics.UpdateAPIView):
    """Контроллер обновления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersDeleteView(generics.DestroyAPIView):
    """Контроллер удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'

