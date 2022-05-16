from django.db import models

class Users(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=20)
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20)

    def __str__(self):
        return self.user_name