from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from slackclient import SlackClient  
from jukebox_core.votingapp.templatetags.url_converter import youtube_embed_url
from jukebox_core.votingapp.models import Songs



SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)
SLACK_BOT_USER_TOKEN = getattr(settings,                          #2
'SLACK_BOT_USER_TOKEN', None)                                     #
Client = SlackClient(SLACK_BOT_USER_TOKEN)                        #3


def get_youtube_link(event_message):
    youtube_urls = []
    if 'message' in event_message:
        if 'attachments' in event_message['message']:
            attachments = event_message['message']['attachments']
            urls = [attachment.get('title_link') for attachment in attachments if attachment.get('service_name') == 'YouTube']
            youtube_urls.extend(urls)
    return youtube_urls
            

class Events(APIView):
    def post(self, request, *args, **kwargs):

        slack_message = request.data

        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)
        # greet bot
        if 'event' in slack_message:                              #4
            event_message = slack_message.get('event')            #
            
            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':     #5
                return Response(status=status.HTTP_200_OK)        #
            
            # process user's message
            # print(event_message)
            user = event_message.get('user')                      #6
            # text = event_message.get('text')                      #
            channel = event_message.get('channel')                #
            bot_text = 'Hi :wave: Youtube links added to the jukebox playlist.'            #
            youtube_urls = get_youtube_link(event_message)
            for url in youtube_urls:
                try:
                    song = Songs(YoutubeLink=url, SongName=str(url))
                    song.save()
                except:
                    pass
                    # bot_text = 'Hi  :wave: Youtube link is already there in jukebox.'
            if youtube_urls:                
                Client.api_call(method='chat.postMessage',        #8
                                channel=channel,                  #
                                text=bot_text)                    #
                return Response(status=status.HTTP_200_OK)        #9

        return Response(status=status.HTTP_200_OK)