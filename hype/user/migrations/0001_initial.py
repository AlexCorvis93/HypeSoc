# Generated by Django 3.2.7 on 2021-11-18 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=90)),
                ('last_name', models.CharField(default='', max_length=90)),
                ('date_birth', models.DateField(max_length=9)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('bio', models.TextField(max_length=140)),
                ('ava', models.ImageField(blank=True, default='add photo', null=True, upload_to='avatar/')),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('login', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('text', models.TextField(verbose_name='text')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Art'), (2, 'business'), (3, 'science ')], verbose_name='category')),
                ('public_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('img', models.ImageField(blank=True, default='add img', null=True, upload_to='posts/')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length='200')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='AnonymusComment',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length='200')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='user.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
