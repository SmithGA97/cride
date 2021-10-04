"""Circles model serializers"""

# Django REST Framework
from rest_framework import serializers

#Models
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """circle model serializer"""
    members_limit = serializers.IntegerField(
        required= False,
        min_value= 10,
        max_value= 32000
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class"""
        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about','picture',
            'rides_offered', 'rides_taken',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )
        read_only_fields = (
            'is_public', 
            'verified',
            'rides_taken',
            'rides_offered'
        )


    def validate(self,data):
        """Ensure both members_limit and is_limit are present"""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)
        if is_limited ^ bool(members_limit):#Si una es False y la otra True, entra a la excepcion
            raise serializers.ValidationError('If circle is limited, a member limit must be provided')
        return data