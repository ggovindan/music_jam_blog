from django.shortcuts import render
from django.views import generic
from . import models

class VBlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2
    