from rest_framework import serializers
from user_management.models import User
from system_management.models import Ticket, City, State


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class CityReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        exclude = ('state', )


class StateReadSerializer(serializers.ModelSerializer):
    cities = CityReadSerializer(many=True, source='city_set')

    class Meta:
        model = State
        fields = '__all__'
