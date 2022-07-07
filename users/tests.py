from django.test import TestCase
from django.urls import reverse
from loguru import logger

from .models import User


class BaseTestCase(TestCase):
    def setUp(self):
        self.register_user_url = reverse('register')
        self.login_page = reverse('login')
        self.user_list = reverse('users')
        self.correct_user_register = {
            'username': 'testusername',
            'first_name': 'testfirstname',
            'last_name': 'testlastname',
            'password': 'Test1234',
            'password2': 'Test1234'
        }
        return super().setUp()

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user('defaultusername1', email=None, password='Test1234',
                                        first_name='defaultfirstname1',
                                        last_name='defaultlastname1')
        user1.save()
        user2 = User.objects.create_user('defaultusername2', email=None, password='Test1234',
                                         first_name='defaultfirstname2',
                                         last_name='defaultlastname2')
        user2.save()

class UserTestCase(BaseTestCase):
    def test_register_user(self):
        self.client.post(self.register_user_url, self.correct_user_register,
                                    format='text/html')
        check_login = self.client.login(username=self.correct_user_register['username'],
                                        password=self.correct_user_register['password'])
        #logger.debug(check_login)

    def test_login(self):
        response = self.client.login(username='defaultusername1', password='Test1234')
        self.assertEqual(response, True)
        response = self.client.login(username='defaultusern2ame1', password='Test1234')
        self.assertEqual(response, False)

    def test_user_list(self):
        response = self.client.get(self.user_list)
        self.assertEqual(response.status_code, 200)
