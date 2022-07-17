# Generated by Django 4.0.4 on 2022-07-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0003_alter_tasks_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', to='labels.labels', verbose_name='Label'),
        ),
    ]
