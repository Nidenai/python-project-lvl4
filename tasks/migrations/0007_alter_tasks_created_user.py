# Generated by Django 4.0.4 on 2022-06-07 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_remove_tasks_created_user_tasks_created_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Автор', to=settings.AUTH_USER_MODEL),
        ),
    ]
