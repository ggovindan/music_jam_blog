from django.db import models
from django.core.urlresolvers import reverse
from embed_video.fields import EmbedVideoField
import uuid
import datetime

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class UpcomingEventQuerySet(models.QuerySet):
    def get_upcoming_events(self):
        return self.filter(event_date__gte=datetime.date.today())

class AboutAuthor(models.QuerySet):
    def published(self):
        print("ABOUTAUTHOR: {}".format(self.all()))
        return self.all()

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=False)

    def __str__(self):
        return self.slug

class About(models.Model):
    image = models.CharField(max_length=200)
    #image = models.ImageField()
    about_body = models.TextField()
    slug = models.SlugField(max_length=200, unique=False)

    objects = AboutAuthor.as_manager()

    def __str__(self):
        return self.image

    def get_absolute_url(self):
        return reverse("about_author", kwargs={"slug": self.slug})

class Entry(models.Model):
    title = models.CharField(max_length=200)
    video = EmbedVideoField(default="")
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    entry_id = models.UUIDField(default=uuid.uuid4, editable=False)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=200)
    entry_id = models.UUIDField(default=uuid.uuid4, editable=False)
    event_date = models.DateField()
    details = models.TextField()
    objects = UpcomingEventQuerySet.as_manager()
    
    def __str__(self):
        return self.title
