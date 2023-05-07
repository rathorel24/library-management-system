from rest_framework import permissions
from .models import UserRole

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.role == UserRole.LIBRARIAN
    
class IsMemeber(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.role == UserRole.MEMBER
