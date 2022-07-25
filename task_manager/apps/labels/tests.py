from django.test import TestCase
from django.urls import reverse

from task_manager.apps.labels.models import Labels
from task_manager.apps.users.models import User


class LabelsTestCase(TestCase):
    fixtures = ['users.json'], ['statuses.json'], \
               ['tasks.json'], ['labels.json']

    def setUp(self):
        self.label_for_test = {
            'name': 'test_labels_name'
        }
        self.label_page = reverse('labels:list')
        self.user = User.objects.get(pk=1)
        self.current_label = Labels.objects.get(pk=1)
        self.another_label = Labels.objects.get(pk=2)
        return super().setUp()

    def test_labels_page(self):
        response = self.client.get(self.label_page)
        self.assertEqual(response.status_code, 302)

    def test_labels_create(self):
        label = {'name': 'Test_Label'}
        self.client.force_login(self.user)
        response = self.client.post(reverse('labels:create'),
                                    label, follow=True)
        self.assertRedirects(response, '/labels/')
        self.assertContains(response, 'Метка успешно создана')

    def test_labels_delete(self):
        labels_for_delete = {'name': 'Label_for_Delete'}
        self.client.force_login(self.user)
        self.client.post(reverse('labels:create'),
                         labels_for_delete, follow=True)
        current_label = Labels.objects.get(pk=6)
        response = self.client.post(reverse('labels:delete',
                                            args=[current_label.id]),
                                    follow=True)
        self.assertRedirects(response, reverse('labels:list'))

    def test_labels_update(self):
        self.client.force_login(self.user)
        update_url = reverse('labels:update',
                             args=(self.current_label.id,))
        updated_label = {'name': 'Что-то новое'}
        response = self.client.post(update_url,
                                    updated_label, follow=True)
        self.assertRedirects(
            response,
            '/labels/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(response, 'Метка успешно изменена')

    def test_delete_using_label(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('labels:delete',
                                            args=(self.another_label.id,)),
                                    follow=True)
        self.assertRedirects(
            response,
            '/labels/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
        self.assertContains(
            response,
            'Невозможно удалить метку, потому что она используется')
