# Generated by Django 4.0.4 on 2022-06-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='label',
        ),
        migrations.AddField(
            model_name='tasks',
            name='label',
            field=models.ManyToManyField(related_name='labels', to='labels.labels', verbose_name='Метка'),
        ),
    ]
