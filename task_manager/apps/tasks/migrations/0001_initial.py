# Generated by Django 4.0.4 on 2022-07-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(max_length=150,
                                          verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True,
                                                 verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
