from celery import shared_task
from .models import *
import base64
from django.core.files.base import ContentFile


@shared_task
def send_chat_file(room_group_name, user, replay_object, file, name, type):
    format, imgstr = str(file).split(';base64,')
    data = ContentFile(base64.b64decode(imgstr), name=name)
    if type == 'pv':
        ChatModel.objects.create(room_id=room_group_name, sender_id=user,
                                 replay=replay_object, file=data)

        ChannelRoomModel.objects.filter(id=room_group_name).update(last_message=name)

    elif type == 'group':
        GroupChatModel.objects.create(room_id=room_group_name, sender_id=user,
                                      replay=replay_object, file=data)
        GroupRoomModel.objects.filter(id=room_group_name).update(last_message=name)

    elif type == 'channel':
        ChannelChatModel.objects.create(room_id=room_group_name, sender_id=user,
                                        replay=replay_object, file=data)
        ChannelRoomModel.objects.filter(id=room_group_name).update(last_message=name)
