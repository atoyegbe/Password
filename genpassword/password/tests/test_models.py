from django.test import TestCase
from password.models import Passwords

class ModelTestCase(TestCase):
    def test_model_str_method(self):
        facebook = Passwords.objects.create(name='Facebook', password='myfacebook')
        github = Passwords.objects.create(name="GitHub", password="pushcode")
        
        self.assertEqual(str(facebook), facebook.name)
        self.assertEqual(str(github), github.name)
    
    def test_verbose_name_plural(self):
        self.assertEqual(str(Passwords._meta.verbose_name_plural), 'passwords')
         