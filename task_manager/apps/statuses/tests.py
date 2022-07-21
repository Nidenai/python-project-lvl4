from django.test import TestCase
from django.urls import reverse

from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


class BaseTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json']

    def setUp(self):
        self.status_for_test = {
            'name': 'test_status_name'
        }
        self.status_page = reverse('statuses:list')
        self.user = User.objects.get(pk=1)
        self.current_status = Status.objects.get(pk=1)
        return super().setUp()


class StatusTestCase(BaseTestCase):
    def test_status_page(self):
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 302)

    def test_status_create(self):
        status = {'name': 'Test_Status'}
        self.client.force_login(self.user)
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('statuses:create'),
                                    status, follow=True)
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, 'Статус успешно создан')
        created_status = Status.objects.get(name=status['name'])
        self.assertEquals(created_status.name, 'Test_Status')

    def test_status_delete(self):
        status_for_delete = {'name': 'Status_for_Delete'}
        self.client.force_login(self.user)
        self.client.post(reverse('statuses:create'),
                         status_for_delete, follow=True)
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 200)
        current_status = Status.objects.get(pk=3)
        response = self.client.post(reverse('statuses:delete',
                                            args=[current_status.id]),
                                    follow=True)
        self.assertRedirects(response, reverse('statuses:list'))