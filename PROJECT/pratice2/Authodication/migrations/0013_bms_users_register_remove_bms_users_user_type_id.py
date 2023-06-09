# Generated by Django 4.1.7 on 2023-03-24 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Authodication', '0012_remove_bms_users_details_role_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bms_Users_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('phone_no', models.CharField(max_length=16)),
                ('birthday', models.DateField(auto_now_add=True)),
                ('address', models.TextField(max_length=2321)),
                ('created_user_details_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_user_details_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bms_user_register_tbl',
            },
        ),
        migrations.RemoveField(
            model_name='bms_users',
            name='user_type_id',
        ),
    ]
