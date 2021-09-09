from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ClassSerializer
from .models import Class
# Create your views here.


class ClassViewSet(viewsets.ModelViewSet):
    ## Give it the main query for the index route
    queryset = Class.objects.all()
    # THe serializer for serializing
    serializer_class = ClassSerializer
    ## Optional Permissions
    permission_classes = [permissions.AllowAny]