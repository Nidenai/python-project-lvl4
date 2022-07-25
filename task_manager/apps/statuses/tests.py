from django.test import TestCase
from django.urls import reverse

from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


class StatusesTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json'], \
               ['tasks.json'], ['labels.json']

    def setUp(self):
        self.status_for_test = {
            'name': 'test_status_name'
        }
        self.status_page = reverse('statuses:list')
        self.user = User.objects.get(pk=1)
        self.current_status = Status.objects.get(pk=1)
        self.another_status = Status.objects.get(pk=2)
        return super().setUp()

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

    def test_status_update(self):
        self.client.force_login(self.user)
        update_url = reverse('statuses:update',
                             args=(self.current_status.id,))
        updated_status = {'name': 'В процессе'}
        response = self.client.post(update_url,
                                    updated_status, follow=True)
        self.assertRedirects(
            response,
            '/statuses/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Статус успешно изменён')

    def test_delete_using_status(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('statuses:delete',
                                            args=(self.another_status.id,)),
                                    follow=True)
        self.assertRedirects(
            response,
            '/statuses/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(
            response,
            'Невозможно удалить статус, потому что он используется')
