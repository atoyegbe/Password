from django.test import TestCase
from password.forms import UserForm

class UserRegistrationForm(TestCase):
    
    def test_registration_invalid_form(self):
        invalid_data = {
            "username": "deyemi",
            "email": "deyemi@test.com",
            "password1": "firsttest",
            "password2": "not firsttest"
        }
        
        form = UserForm(data=invalid_data)
        self.assertFalse(form.is_valid())
    
    def test_registration_valid_form(self):
        valid_data = {
            "username": "deyemi",
            "email": "deyemi@test.com",
            "password1": "firsttest",
            "password2": "firsttest"
        }
        form = UserForm(data=valid_data)
        self.assertTrue(form.is_valid())