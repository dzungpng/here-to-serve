# Generated by Django 3.0.4 on 2020-05-15 01:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventActivity',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.Activity')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MealActivity',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.Activity')),
                ('delivery_time', models.TimeField(blank=True, null=True)),
                ('delivery_location', models.CharField(blank=True, default='', max_length=150)),
                ('dietary_restrictions', models.CharField(blank=True, default='None', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='RideActivity',
            fields=[
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.Activity')),
                ('pickup_time', models.TimeField(blank=True, null=True)),
                ('pickup_time_buffer', models.TimeField(blank=True, null=True)),
                ('arrive_time', models.TimeField(blank=True, null=True)),
                ('pickup_location', models.CharField(blank=True, default='', max_length=150)),
                ('destination_location', models.CharField(blank=True, default='', max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='arrive_time',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='custom_repeat_dates',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='delivery_between',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='delivery_location',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='dietary_restrictions',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='display_type',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='location',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='pickup_between',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='pickup_location',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='pickup_time',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='repeat',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='role',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='weekly_repeat_dates',
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(choices=[('Giving Rides', 'Giving Rides'), ('Preparing Meals', 'Preparing Meals'), ('Shopping', 'Shopping'), ('Childcare', 'Childcare'), ('Visits', 'Visits'), ('Coverage', 'Coverage'), ('Miscellaneous', 'Miscellaneous'), ('Occassion', 'Occassion')], default='Occassion', max_length=20),
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='activity',
            name='event_batch',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='activity',
            name='is_recurring',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='est_hours',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='est_minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='volunteers_needed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='volunteers_signed_up',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
