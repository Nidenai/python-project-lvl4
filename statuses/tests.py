from django.test import TestCase
from django.urls import reverse
from loguru import logger

from statuses.models import Statuses
from users.models import User


class BaseTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json']

    def setUp(self):
        self.status_for_test = {
            'status_name': 'test_status_name'
        }
        self.status_page = reverse('statuses')
        self.user = User.objects.get(pk=1)
        return super().setUp()



class StatusTestCase(BaseTestCase):
    def test_status_page(self):
        response = self.client.get(self.status_page)
        self.assertEqual(response.status_code, 200)


    def test_status_create(self):
        status = {'name': 'Test_Status'}
        self.client.force_login(self.user)
        self.client.post(reverse('add_s'), status, follow=True)
        response = self.client.get(self.status_page)
        response_tasks = list(response.context['statuses'])
        logger.debug(response_tasks)
