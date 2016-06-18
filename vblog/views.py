from django.shortcuts import render
from django.views import generic
from . import models

class VBlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

class VBlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "entry_detail.html"

class About(generic.ListView):
    queryset = models.About.objects.published()
    print("inside About view queryset={}".format(queryset))
    model = models.About
    template_name = "About.html"
