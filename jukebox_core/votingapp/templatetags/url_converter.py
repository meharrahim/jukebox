from django import template
from django.conf import settings
register = template.Library()
import re

@register.filter(name='youtube_embed_url')
# converts youtube URL into embed HTML
# value is url
def youtube_embed_url(value):
    match = re.search(r'^(http|https)\:\/\/www\.youtube\.com\/watch\?v\=(\w*)(\&(.*))?$', value)
    if match:
        embed_url = 'http://www.youtube.com/embed/%s' %(match.group(2))
        res = "<iframe width=\"200\" height=\"113\" src=\"%s\" frameborder=\"0\" allowfullscreen></iframe>" %(embed_url)
        return res
    return ''

youtube_embed_url.is_safe = True