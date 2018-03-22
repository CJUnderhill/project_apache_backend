from rest_framework.permissions import BasePermission

from .models import Complaint


# Create permissions here.

class IsOwner(BasePermission):
    """Custom permissions class to allow only complaint owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the complaint owner."""
        if isinstance(obj, Complaint):
            return obj.owner == request.user
        return obj.owner == request.user
