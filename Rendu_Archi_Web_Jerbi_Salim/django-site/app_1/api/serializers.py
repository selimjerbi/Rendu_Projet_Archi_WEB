from rest_framework import serializers
from .models import IntegrationWeekend, Service, Registration, ServiceChoice

class IntegrationWeekendSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegrationWeekend
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ServiceChoice.objects.all(),
        required=False
    )

    class Meta:
        model = Registration
        fields = '__all__'

class ServiceChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceChoice
        fields = '__all__'
