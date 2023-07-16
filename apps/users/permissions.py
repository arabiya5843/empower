from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoObjectPermissions


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_superuser)


class IsAdminUserOrEmployerReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.type == 'employer' and request.user.is_superuser)


class IsEmployeeOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.type == "employee"


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.type == 'employee')

    def has_object_permission(self, request, view, obj):
        if obj.user.type == 'employee' and request.user:
            return True
        return False


class IsEmployer(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.type == 'employer')


class CustomDjangoObjectPermissions(DjangoObjectPermissions):
    perms_map = {
        # 'GET': ['%(app_label)s.view_%(model_name)s', '%(app_label)s.see_premium_%(model_name)s', ],
        'GET': ['%(app_label)s.see_premium_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsEmployerOrReadOnlyOrAdminUser(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return bool(request.user and request.user.is_superuser)
        else:
            return bool(request.method in SAFE_METHODS or request.user and request.user.type == 'employer')


class IsEmployerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.EMPLOYER == request.user