from . import models
from . import serializers
from rest_framework import viewsets, permissions


class EmailViewSet(viewsets.ModelViewSet):
    """ViewSet for the Email class"""
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer