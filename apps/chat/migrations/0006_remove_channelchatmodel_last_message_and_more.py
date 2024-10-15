# Generated by Django 5.1.1 on 2024-10-11 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chatmodel_replay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channelchatmodel',
            name='last_message',
        ),
        migrations.AddField(
            model_name='channelchatmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='group/files'),
        ),
        migrations.AddField(
            model_name='channelchatmodel',
            name='replay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chat.chatmodel'),
        ),
        migrations.AddField(
            model_name='channelroommodel',
            name='last_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='pv/files'),
        ),
        migrations.AddField(
            model_name='groupchatmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='group/files'),
        ),
        migrations.AddField(
            model_name='groupchatmodel',
            name='replay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chat.chatmodel'),
        ),
        migrations.AlterField(
            model_name='channelchatmodel',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groupchatmodel',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
