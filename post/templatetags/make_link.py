import re

from django import template

register = template.Library()


@register.filter
def hashtag_link(post):
    content = post.content
    for hashtag in post.hashtags.all():
        content = re.sub(
            fr'{hashtag.content}\b',
            f'<a href="/post/hashtags/{hashtag.id}/">{hashtag.content}</a>',
            content)
    return content
