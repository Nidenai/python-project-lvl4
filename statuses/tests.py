from django.test import TestCase
from django.urls import reverse
from loguru import logger

from users.models import User
from statuses.models import Status


class BaseTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json']

    def setUp(self):
        self.status_for_test = {
            'status_name': 'test_status_name'
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
        status = {'status_name': 'Test_Status'}
        self.client.force_login(self.user)
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('statuses:create'), status, follow=True)
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, 'Статус успешно создан')
        created_status = Status.objects.get(status_name=status['status_name'])
        #logger.debug(created_status)
        self.assertEquals(created_status.status_name, 'Test_Status')

    def test_status_delete(self):
        status_for_delete = {'status_name': 'Status_for_Delete'}
        self.client.force_login(self.user)
        self.client.post(reverse('statuses:create'), status_for_delete, follow=True)
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 200)
        current_status = Status.objects.get(pk=3)
        logger.debug(current_status.id)
        response = self.client.post(reverse('statuses:delete', args=[current_status.id]), follow=True)
        self.assertRedirects(response, reverse('statuses:list'))