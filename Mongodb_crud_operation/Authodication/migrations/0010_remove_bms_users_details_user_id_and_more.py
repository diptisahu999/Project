# Generated by Django 4.1.7 on 2023-03-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authodication', '0009_bms_users_details_department_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bms_users_details',
            name='user_id',
        ),
        migrations.AddField(
            model_name='bms_users',
            name='user_details',
            field=models.ManyToManyField(related_name='abc', to='Authodication.bms_users_details'),
        ),
    ]
