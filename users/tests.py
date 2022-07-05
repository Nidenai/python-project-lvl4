from django.test import TestCase
from django.urls import reverse

from .models import *


class TestUsersCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('test_user', email=None, password='QazWsx741', first_name='test',
                                        last_name='user')
        user.save()

    def test_user_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['users'])
        self.assertQuerysetEqual(response_tasks, ['<User: test user>'])

    def test_registration_user(self):
        user_for_test = {
            'first_name': 'MyName',
            'last_name': 'MyLastName',
            'username': 'Username',
            'password1': 'Qwerty789',
            'password2': 'Qwerty789'
        }
        register_url = reverse('register')
        response = self.client.post(register_url, user_for_test, follow=True)
        response_tasks = list(self.client.get(reverse('users')).context['users'])
        print(response_tasks)
        #self.assertRedirects(response, '/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        #self.assertContains(response, 'Пользователь успешно зарегистрирован')
