from rest_framework import serializers
from .models import UserData
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=UserData.objects.all())])
    class Meta:
        model = UserData
        fields = '__all__'

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.save()
        return user

    