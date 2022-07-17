from django.test import TestCase
from django.urls import reverse

from statuses.models import Status
from users.models import User


class BaseTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json'], \
               ['tasks.json'], ['labels.json']

    def setUp(self):
        self.task_for_test = {
            'task_name': 'test_task_name'
        }
        self.status_page = reverse('statuses:list')
        self.user = User.objects.get(pk=1)
        self.current_status = Status.objects.get(pk=1)
        return super().setUp()
