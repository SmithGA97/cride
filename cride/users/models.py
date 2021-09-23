"""User model"""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField

#Utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """User model
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields
    """

    email = models.EmailField(
        'email_address', 
        unique=True,
        error_messages={
            'unique': 'A user with that email alredy exists'
        }
    )

    phone_number = CharField(
        max_length=17,
        blank=True
    )
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['username', 'first_name', 'last_name']


    is_client = models.BooleanField(
        'client_status',
        default=True,
        help_text=(
            'Help easily distinguish user and perform queries. '
            'Clients are the main type of user.'
        )
    )
    is_verified= models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified email address'
    )