""""Circles views"""

#Django REst Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Serializers
from cride.circles.serializers import CircleSerializer, CreateCircleSerializer

#Models
from cride.circles.models import Circle

@api_view(['GET'])
def list_circles(request):
    """list circles"""
    circles = Circle.objects.all().filter(is_public=True)
    serializer = CircleSerializer(circles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_circle(request):
    """Create circle"""
    #import ipdb; ipdb.set_trace()
    serializer = CreateCircleSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    circle = serializer.save()
    return Response(CircleSerializer(circle).data)