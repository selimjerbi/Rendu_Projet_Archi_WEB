from django.urls import include, path
from rest_framework import routers
from .views import (
    IntegrationWeekendViewSet, ServiceViewSet, 
    RegistrationViewSet, ServiceChoiceViewSet
)

router = routers.DefaultRouter()
router.register(r'weekends', IntegrationWeekendViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'registrations', RegistrationViewSet)
router.register(r'service-choices', ServiceChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
