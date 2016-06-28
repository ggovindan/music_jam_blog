from django.db import models
from django.core.urlresolvers import reverse
from embed_video.fields import EmbedVideoField
import uuid
from datetime import date
from django.utils import timezone

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class EventQuerySet(models.QuerySet):
    def latest(self):
        return self.all().filter(event_date__gt=timezone.now())

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=False)

    def __str__(self):
        return self.slug


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

class UpcomingEvents(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    event_date = models.DateTimeField(default=date.today)
    objects = EventQuerySet.as_manager()
