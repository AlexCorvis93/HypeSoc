# Generated by Django 3.2.7 on 2021-11-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymus', '0002_auto_20211118_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymuscomment',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
