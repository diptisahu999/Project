# Generated by Django 4.1.7 on 2023-03-23 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authodication', '0011_alter_bms_users_details_department_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bms_users_details',
            name='role_id',
        ),
    ]
