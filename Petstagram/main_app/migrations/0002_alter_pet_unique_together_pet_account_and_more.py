# Generated by Django 4.0.4 on 2022-07-31 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('name',)},
        ),
        migrations.AddField(
            model_name='pet',
            name='account',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pet',
            name='user_profile',
        ),
    ]