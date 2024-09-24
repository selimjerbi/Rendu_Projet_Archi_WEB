from rest_framework import viewsets
from .models import IntegrationWeekend, Service, Registration, ServiceChoice
from .serializers import (
    IntegrationWeekendSerializer, ServiceSerializer, 
    RegistrationSerializer, ServiceChoiceSerializer
)

class IntegrationWeekendViewSet(viewsets.ModelViewSet):
    queryset = IntegrationWeekend.objects.all()
    serializer_class = IntegrationWeekendSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class ServiceChoiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceChoice.objects.all()
    serializer_class = ServiceChoiceSerializer
