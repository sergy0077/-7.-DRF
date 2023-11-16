from django.shortcuts import render
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать свои объекты, но только чтение для других.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить чтение для всех запросов
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить запись только владельцу объекта
        return obj.user == request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_object_permission():
            return render(request, 'habits/access_denied.html')
        return super().dispatch(request, *args, **kwargs)
