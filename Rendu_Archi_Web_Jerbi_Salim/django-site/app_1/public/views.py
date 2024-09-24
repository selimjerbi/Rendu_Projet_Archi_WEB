from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from api.models import IntegrationWeekend, Service, Registration, ServiceChoice
from django.contrib.auth import logout
from .forms import ServiceForm
from .forms import UpdateDescriptionForm

def home(request):
    return render(request, 'public/home.html')

def description(request):
    weekend = IntegrationWeekend.objects.first()
    return render(request, 'public/description.html', {'weekend': weekend})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Connexion automatique après inscription
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'public/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'public/login.html', {'form': form})

@login_required
def welcome(request):
    services = Service.objects.all()  # Récupérer tous les services
    return render(request, 'public/welcome.html', {'services': services})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')  # Redirige vers la page de bienvenue après l'ajout
    else:
        form = ServiceForm()
    return render(request, 'public/add_service.html', {'form': form})

def update_description(request):
    # Obtenez l'objet IntegrationWeekend que vous voulez mettre à jour
    weekend = get_object_or_404(IntegrationWeekend, pk=1)  # Ajustez l'ID selon vos besoins

    if request.method == "POST":
        form = UpdateDescriptionForm(request.POST, instance=weekend)
        if form.is_valid():
            form.save()
            return redirect('description')  # Redirige vers la page de description après la mise à jour
    else:
        form = UpdateDescriptionForm(instance=weekend)

    return render(request, 'public/description.html', {'form': form, 'weekend': weekend})