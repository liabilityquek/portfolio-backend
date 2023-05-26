from rest_framework import serializers
from .models import *

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'