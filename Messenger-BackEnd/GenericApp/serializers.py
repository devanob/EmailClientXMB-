from . import models

from rest_framework import serializers


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Email
        fields = (
            'pk', 
            'message', 
            'subject', 
            'date', 
            'fromEmail', 
            'toEmail', 
            'isArchived', 
        )

