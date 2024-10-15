# Generated by Django 5.1.1 on 2024-10-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_usermodel_add_channel_and_more'),
    ]

    operations = [
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
    ]
