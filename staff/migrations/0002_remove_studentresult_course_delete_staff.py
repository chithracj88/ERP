# Generated by Django 4.0.6 on 2022-08-19 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentresult',
            name='course',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]