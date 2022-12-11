# Generated by Django 4.0.4 on 2022-06-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0003_profile_dailyroutine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dailyRoutine',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dailyRoutine', to='webapi.routine'),
        ),
    ]