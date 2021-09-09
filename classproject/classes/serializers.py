from .models import Class 
from rest_framework import serializers

class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        # which fields should be serialized
        fields = ["id","title", "platform", "length"]
