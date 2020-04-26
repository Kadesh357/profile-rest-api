from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow userto edit thieir own Profile"""

    def has_object_permission(self, request ,view ,obj):
        """Checkuser is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
