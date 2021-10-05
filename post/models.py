from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class HashTag(models.Model):
    content = models.CharField(max_length=100)


class Post(models.Model):
    content = models.TextField()
    image = ProcessedImageField(
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90},
        upload_to='media'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(HashTag, related_name='taged_post')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts'
    )


class Comment(models.Model):
    content = models.CharField(max_length=250)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
