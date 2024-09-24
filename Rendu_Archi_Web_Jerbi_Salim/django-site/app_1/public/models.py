from django.contrib.auth.models import User
from django.db import models

class IntegrationWeekend(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ServiceChoice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.service.name

class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='public_registrations')
    weekend = models.ForeignKey(IntegrationWeekend, on_delete=models.CASCADE)
    services = models.ManyToManyField(ServiceChoice, blank=True, related_name='public_registrations')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.weekend.title}"
