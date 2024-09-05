# Generated by Django 5.1.1 on 2024-09-05 15:15

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_usermodel_add_channel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='favorite_contacts',
        ),
        migrations.AddField(
            model_name='customuser',
            name='family_name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='add_channel',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='add_group',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='bio_seen',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='find_with_phone',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_seen',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='profile_seen',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='story_seen',
            field=models.CharField(choices=[('all', 'All'), ('contacts', 'Contacts'), ('no_one', 'No One')], default='all', max_length=1000),
        ),
        migrations.CreateModel(
            name='UserContactsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('family_name', models.CharField(max_length=64)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_contacts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_contacts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to_favorites', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='user/file')),
                ('title', models.CharField(max_length=1000)),
                ('date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_files', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGifModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='user/gif')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_gifs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
