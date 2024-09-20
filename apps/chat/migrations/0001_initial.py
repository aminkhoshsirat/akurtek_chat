# Generated by Django 5.1.1 on 2024-09-08 12:04

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelAdminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add_admin', models.BooleanField(default=False)),
                ('can_delete_message', models.BooleanField(default=False)),
                ('can_change_info', models.BooleanField(default=False)),
                ('can_add_user', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('edited', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('last_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='channel/image')),
                ('private', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=10000, unique=True)),
                ('add_member', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('edited', models.TextField(blank=True, null=True)),
                ('last_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupAdminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_add_admin', models.BooleanField(default=False)),
                ('can_delete_message', models.BooleanField(default=False)),
                ('can_change_info', models.BooleanField(default=False)),
                ('can_add_user', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('edited', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('last_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='group/image')),
                ('private', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=10000, unique=True)),
                ('add_member', models.BooleanField(default=True)),
            ],
        ),
    ]
