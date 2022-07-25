from django.test import TestCase
from django.urls import reverse

from task_manager.apps.labels.models import Labels
from task_manager.apps.statuses.models import Status
from task_manager.apps.tasks.models import Tasks
from task_manager.apps.users.models import User


class TaskTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json'], \
               ['tasks.json'], ['labels.json']

    def setUp(self):
        self.first_task = Tasks.objects.get(pk=1)
        self.second_task = Tasks.objects.get(pk=2)
        self.third_task = Tasks.objects.get(pk=3)
        self.fourth_task = Tasks.objects.get(pk=4)
        self.status_for_task = Status.objects.get(pk=1)
        self.executor = User.objects.get(pk=1)
        self.author = User.objects.get(pk=2)
        self.label_for_task = Labels.objects.get(pk=1)
        self.new_task = {
            'name': 'New Task',
            'description': 'New task description',
            'status': self.status_for_task,
            'executor': self.executor,
            'label': [self.label_for_task],
        }

    def test_list_of_tasks(self):
        self.client.force_login(self.author)
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, 200)
        response_tasks = list(response.context['tasks'])
        self.assertQuerysetEqual(response_tasks,
                                 [self.first_task, self.second_task,
                                  self.third_task, self.fourth_task])

    def create_update_and_delete_task(self):
        """Проверка создания задачи."""
        self.client.force_login(self.author)
        response = self.client.post(reverse('tasks:create'),
                                    self.new_task, follow=True)
        self.assertRedirects(
            response,
            '/tasks/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Задача успешно создана')
        created_task = Tasks.objects.get(name=self.new_task['name'])
        self.assertEquals(created_task.name, 'New Task')
        """Проверка изменения задачи"""
        response = self.client.post(reverse('tasks:update'),
                                    self.new_task_data, follow=True)
        self.assertRedirects(
            response,
            '/tasks/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Задача успешно изменена')
        """Проверка удаления задачи"""
        delete_url = reverse('tasks:delete', args=5)
        response = self.client.post(delete_url, follow=True)
        self.assertRedirects(
            response,
            '/tasks/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Задача успешно удалена')

    def test_delete_another_user(self):
        self.client.force_login(self.executor)
        delete_url = reverse('tasks:delete', args=(self.first_task.id, ))
        response = self.client.post(delete_url, follow=True)
        self.assertTrue(Tasks.objects.filter(pk=self.first_task.id).exists())
        self.assertRedirects(
            response,
            '/tasks/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Задачу может удалить только её автор')
