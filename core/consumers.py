import json
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
# import time

# from django.core.mail import send_mail

@channel_session_user_from_http
def ws_connect(message):
    # Accept the connection
    if message.user.id != None:
        message.reply_channel.send({"accept": True})
        # Add to the chat group
        Group(message.content['path'].replace("/","_")+str(message.user.company_id)).add(message.reply_channel)
    else:
        message.reply_channel.send({"accept": False})


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    if message.user.id != None:
        Group(message.content['path'].replace("/","_")+str(message.user.company_id)).discard(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group(message.content['path'].replace("/","_")+str(message.user.company_id)).send({'text': json.dumps({'message': message.content['text'],
                                            'sender': message.reply_channel.name})})
