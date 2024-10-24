from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# crear el test

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test','test@gmail.com','test123456')
    def test_profile_exist(self):
        exists = Profile.objects.filter(user__username= 'test').exists()
        self.assertEqual(exists,True)
    
