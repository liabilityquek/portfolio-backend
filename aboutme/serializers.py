from .models import *
from rest_framework import serializers

class Profile_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
