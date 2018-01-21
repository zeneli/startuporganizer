from django.core.urlresolvers import reverse
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name.title()


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']
        # Latest startups are the ones most recently founded.
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        # Latest news links are the onces most recently published.
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)
