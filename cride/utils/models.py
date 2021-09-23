"""Django models utilities"""

#Django
from django.db import models

class CRideModel(models.Model):
    """Comparte ride base model
    
    CRide models acts as an abstract base class from which every 
    other model in the project will inherance. This class provides
    every table with the following atributes:
        + created (DateTime): Store the datetime the object was created
        + modified (DateTime): Store the last datetime the object was modified
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add= True,
        help_text='Date time on which the object was created'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now_add= True,
        help_text='Date time on which the object was modified'
    )

    class Meta:
        """Meta option"""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']


