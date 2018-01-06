from django.db import models
from organizer.models import Startup, Tag

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=31,
        unique_for_month='pub_date',
        help_text='A label for URL config.'
    )
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')
