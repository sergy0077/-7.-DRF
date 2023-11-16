from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserCreationApiView, UsersCreateView, UsersListView, UsersDetailView, UsersUpdateView, UsersDeleteView
from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserCreationApiView.as_view(), name='user_create'),
    path("registration/", UsersCreateView.as_view(), name='registration'),
    path("list/", UsersListView.as_view(), name='users_list'),
    path("<str:username>/", UsersDetailView.as_view(), name='users_detail'),
    path("<str:username>/update/", UsersUpdateView.as_view(), name='users_update'),
    path("<str:username>/delete/", UsersDeleteView.as_view(), name='users_delete'),
]

