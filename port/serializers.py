from .models import *
from rest_framework import serializers

class Portfolio_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
