# Generated by Django 4.0.4 on 2022-06-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labels',
            name='label_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Имя'),
        ),
    ]