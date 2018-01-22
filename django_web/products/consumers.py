from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" %
                            message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


@channel_session
def ws_connect(message, room_name):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    print("Connected")
    Group("product-%s" % room_name).add(message.reply_channel)


@channel_session
def ws_message(message, room_name):
    print("Send message", message)
    Group("product-%s" % room_name).send({
        "text": message.content['text'],
    })


@channel_session
def ws_disconnect(message, room_name):
    print("Disconnect", message)
    Group("product-%s" % room_name).discard(message.reply_channel)
