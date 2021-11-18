# Generated by Django 3.2.7 on 2021-11-18 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anonymus', '0003_alter_anonymuscomment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymuscomment',
            name='name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
