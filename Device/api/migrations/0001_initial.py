# Generated by Django 4.1.7 on 2023-03-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'area_tbl',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area')),
            ],
            options={
                'db_table': 'department_tbl',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=150)),
                ('device_type', models.CharField(max_length=150)),
                ('app_type', models.CharField(max_length=150)),
                ('device_object', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'db_table': 'devices_tbl',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('icon_type', models.CharField(choices=[('scenes_icons', 'Scene'), ('device_icons', 'Device')], max_length=150)),
            ],
            options={
                'db_table': 'icon_tbl',
            },
        ),
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('on_image_path', models.CharField(max_length=255)),
                ('off_image_path', models.CharField(max_length=255)),
                ('width', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.department')),
            ],
            options={
                'db_table': 'subArea_tbl',
            },
        ),
        migrations.CreateModel(
            name='STBChannels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOk', models.CharField(max_length=150)),
                ('channels_object', models.JSONField(blank=True, default=list, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.devices')),
            ],
            options={
                'db_table': 'STB_channels_tbl',
            },
        ),
        migrations.AddField(
            model_name='devices',
            name='sub_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subarea'),
        ),
        migrations.CreateModel(
            name='CroppedArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=150)),
                ('crop_image_path', models.CharField(max_length=255)),
                ('moveto', models.BooleanField()),
                ('shape_type', models.CharField(max_length=150)),
                ('isInteractive', models.BooleanField()),
                ('crop_object', models.JSONField(blank=True, default=dict, null=True)),
                ('index_number', models.IntegerField(blank=True, null=True)),
                ('sub_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subarea')),
            ],
            options={
                'db_table': 'cropped_area_tbl',
            },
        ),
    ]
