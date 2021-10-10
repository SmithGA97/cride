""""Ride views"""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from cride.circles.permissions.memberships import IsActiveCircleMember
from rest_framework.permissions import IsAuthenticated

# Serializers
from cride.rides.serializers import CreateRideSerializer

# Models
from cride.circles.models import Circle

class RideViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Ride view set"""

    serializer_class = CreateRideSerializer
    permission_classess = [IsAuthenticated, IsActiveCircleMember]

    def dispatch(self, request, *args, **kwargs): #Con esto apenas se instancie se realiza la verificacion del circulo, en este caso el slug_name
            """"Verify that the circle exists"""
            slug_name = kwargs['slug_name']
            self.circle = get_object_or_404(Circle, slug_name = slug_name )
            return super(RideViewSet, self).dispatch(request, *args, **kwargs)

