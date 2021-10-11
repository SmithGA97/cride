""""Rides permissions
"""

#Django REST Framework
from rest_framework.permissions import BasePermission

class IsRideOwner(BasePermission):
    """Verify requesting user in the ride create"""

    def has_object_permission(self, request, view, obj):
        """Verify requesting user in the ride creator"""
        return request.user == obj.offered_by

class IsNotRideOwner(BasePermission):
    """"Verify the passenger is not owner of ride"""

    message = "The ride owner can't be a passenger."
    def has_object_permission(self, request, view, obj):
        """Check request user doesn't equal to obj"""

        return request.user != obj.offered_by