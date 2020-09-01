from django.test import Client, SimpleTestCase
from django.urls import reverse, resolve
from password.views import home, passwordsView, registerView, loginView



class UrlTestCase(SimpleTestCase):
    def SetUp(self):
        self.client = Client()
        
    def test_hompage(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, home)
    
    def test_passwords_page(self):
        url = reverse('passwords')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(resolve(url).func, passwordsView)
    
    def test_register_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(resolve(url).func, registerView)
    
