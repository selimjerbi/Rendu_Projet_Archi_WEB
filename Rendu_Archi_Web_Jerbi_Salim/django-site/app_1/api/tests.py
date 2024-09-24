from django.test import TestCase, Client
from django.contrib.auth.models import User
from public.models import IntegrationWeekend, Service, Registration, ServiceChoice

class APIViewsTest(TestCase):

    def setUp(self):
        # Création de données de test
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        self.weekend = IntegrationWeekend.objects.create(
            title='Test Weekend',
            description='A weekend for testing',
            start_date='2024-09-01',
            end_date='2024-09-03'
        )
        
        self.service = Service.objects.create(
            name='Test Service',
            description='A service for testing',
            price=100.00
        )
        
        self.service_choice = ServiceChoice.objects.create(
            service=self.service,
            description='Service choice for testing'
        )
        
        self.registration = Registration.objects.create(
            user=self.user,
            weekend=self.weekend
        )
        # Ajoute le ServiceChoice à l'enregistrement
        self.registration.services.add(self.service_choice)

    def test_login(self):
        response = self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Redirection après connexion
        self.assertIn('_auth_user_id', self.client.session)  # Vérifie que l'utilisateur est connecté

    def test_register(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/register/', {'services': [self.service_choice.id]})
        self.assertEqual(response.status_code, 302)  # Redirection après inscription
        self.assertTrue(Registration.objects.filter(user=self.user, weekend=self.weekend).exists())
        self.assertTrue(self.registration.services.filter(id=self.service_choice.id).exists())

    def test_description(self):
        response = self.client.get('/description/')
        self.assertEqual(response.status_code, 200)  # Page de description accessible
        self.assertContains(response, 'Test Weekend')

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/accounts/logout/')
        self.assertEqual(response.status_code, 302)  # Redirection après déconnexion
        self.assertNotIn('_auth_user_id', self.client.session)  # Vérifie que l'utilisateur est déconnecté
