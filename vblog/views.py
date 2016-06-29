from django.shortcuts import render
from django.views import generic
from . import models
#suppot for pagination


class VBlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    context_object_name = "entry_list" # This will be the value used in the template to refer to the list
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super(VBlogIndex, self).get_context_data(**kwargs)
        context['event_list'] = models.UpcomingEvent.objects.get_upcoming_events()
        return context

class VBlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "entry_detail.html"

class UpcomingEvents(generic.ListView):
    queryset = models.UpcomingEvent.objects.get_upcoming_events()
    model = models.UpcomingEvent
    template_name = "content.html"
    context_object_name = "event_list"

class EventDetail(generic.DetailView):
    model = models.UpcomingEvent
    template_name = "event_detail.html"
