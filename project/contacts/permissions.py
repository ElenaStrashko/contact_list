from rest_framework import permissions

from .models import Role


class IsOperationAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        user_role = Role.objects.get(user=request.user)

        if view.action in ['list', 'retrieve']:
            return True

        elif view.action == 'create':
            if user_role.permission in ['ReadAdd', 'ReadAddDelete']:
                return True
            else:
                return False

        elif view.action == 'destroy':
            if user_role.permission == 'ReadAddDelete':
                return True
            else:
                return False
