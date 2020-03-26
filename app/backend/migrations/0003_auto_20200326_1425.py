# Generated by Django 3.0.4 on 2020-03-26 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_communityuserrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityuserrole',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Community'),
        ),
        migrations.AlterField(
            model_name='communityuserrole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]