from rest_framework.permissions import BasePermission

from apps.users.models import User


class IsUserOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.pk == request.user.pk


class IsEmployerAndIsOwnerOfVacancy(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.Type.EMPLOYER

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.user == request.user
