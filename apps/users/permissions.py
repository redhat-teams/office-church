from rest_framework.permissions import BasePermission

class IsAdminOrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or
            getattr(request.user, "role", "") in ("admin", "staff")
        )

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser or
            getattr(request.user, "role", "") == "admin"
        )
