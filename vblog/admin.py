from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from vblog.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage as FlatPageOrig
from django.utils.translation import ugettext_lazy as _

class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class EventAdmin(MarkdownModelAdmin):
    list_display = ("title", "event_date")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

class ExtendedFlatpageForm(FlatpageForm):
    class Meta:
        model = FlatPage
        fields = '__all__'

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', 'image')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
admin.site.register(models.UpcomingEvent, EventAdmin)

admin.site.unregister(FlatPageOrig)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)