from django.test import  TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from password.models import Passwords
from password.views import home, passwordsView, registerView, loginView

class ViewTest(TestCase):
    def SetUp(self):
        self.user = User.objects.create('testUser')
        self.user.set_password('newuser')
        self.user.save()
        self.client = Client()
        self.first_password = Passwords.objects.create(name='Facebook', password='sociallife')
    
    def test_home_view_get(self):
        """ Returning the homepage """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
    
    def test_password_view_get(self):
        """ Password View test: Returning list of saved passwords """
        self.client.login(username='testUser', password='newuser')
        url = reverse('passwords')
        data = Passwords.objects.all()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('main.html')