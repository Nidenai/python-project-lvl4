from django.contrib import auth
from django.test import TestCase
from django.urls import reverse

from .models import User


class UserTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.first_user = User.objects.get(pk=1)
        self.second_user = User.objects.get(pk=2)
        self.third_user = User.objects.get(pk=3)
        self.fourth_user = User.objects.get(pk=4)

    def test_user_page(self):
        response = self.client.get(reverse('users:users'))
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['users'])
        self.assertQuerysetEqual(response_tasks,
                                 [self.first_user, self.second_user,
                                  self.third_user, self.fourth_user])

    def test_create_login_and_delete(self):
        """Проверка регистрации."""
        url = reverse('users:register')
        user = {
            'first_name': 'Алекс',
            'last_name': 'Шевченко',
            'username': 'tester',
            'password1': 'QazWsx753',
            'password2': 'QazWsx753',
        }
        response = self.client.post(url, user, follow=True)
        self.assertRedirects(
            response,
            '/login/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Пользователь успешно зарегистрирован')
        """Проверка авторизации."""
        user = {
            'username': 'tester',
            'password': 'QazWsx753',
        }
        response = self.client.post(reverse('login'), user, follow=True)
        self.assertRedirects(
            response, status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
            expected_url='/'
        )
        """Проверка удаления созданного пользователя."""
        response = self.client.post(reverse('users:delete',
                                            args=(5,)), follow=True)
        self.assertRedirects(
            response,
            '/users/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Пользователь успешно удалён')

    def test_sign_out(self):
        self.client.force_login(self.first_user)
        response = self.client.post(reverse('logout'), follow=True)
        self.assertRedirects(
            response, expected_url='/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertFalse(auth.get_user(self.client).is_authenticated)
        self.assertContains(response, 'Вы разлогинены')
