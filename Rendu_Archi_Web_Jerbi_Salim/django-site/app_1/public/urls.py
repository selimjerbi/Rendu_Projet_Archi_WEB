from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('description/', views.update_description, name='description'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('add-service/', views.add_service, name='add_service'),
]

