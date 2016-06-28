from django.shortcuts import render
from django.views import generic
from . import models
#suppot for pagination


class VBlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    context_object_name = "entry_list" # This will be the value used in the template to refer to the list
    paginate_by = 4

class VBlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "entry_detail.html"

class UpcomingEvents(generic.ListView):
    queryset = models.UpcomingEvents.objects.latest()
    paginated_by = 4
    template_name = "content.html"
    context_object_name = "upcoming_events"
