# from django.contrib import admin
# from django_markdown.admin import MarkdownModelAdmin
# from . import models
# 
# #class EntryAdmin(admin.ModelAdmin):
# class EntryAdmin(admin.ModelAdmin):
#     list_display = ("title", "created")
#     prepopulated_fields = {"slug": ("title",)}
# 
# admin.site.register(models.Entry, EntryAdmin)


from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.Entry, EntryAdmin)
#admin.site.register(models.Tag)
