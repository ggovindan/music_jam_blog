from django.shortcuts import render
from django.views import generic
from . import models
#suppot for pagination

#The following is a copy from django.contrib.flatpages.views
#in order to make About.html work with my version of Flatpage model
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

DEFAULT_TEMPLATE = 'flatpages/default.html'


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

    def get_context_data(self, **kwargs):
        context = super(VBlogDetail, self).get_context_data(**kwargs)
        context['event_list'] = models.UpcomingEvent.objects.get_upcoming_events()
        return context

class UpcomingEvents(generic.ListView):
    queryset = models.UpcomingEvent.objects.get_upcoming_events()
    model = models.UpcomingEvent
    template_name = "content.html"
    context_object_name = "event_list"

class EventDetail(generic.DetailView):
    model = models.UpcomingEvent
    template_name = "event_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['event_list'] = models.UpcomingEvent.objects.get_upcoming_events()
        return context

#The following is a copy from django.contrib.flatpages.views
#in order to make About.html work with my version of Flatpage model
def flatpage(request, url):
    """
    Public interface to the flat page view specific to About and contact.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or :template:`flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    try:
        f = get_object_or_404(models.FlatPage,
            url=url, sites=site_id)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(models.FlatPage,
                url=url, sites=site_id)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, f):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        template = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    print("type(f)={}".format(type(f)))
    print("dir(f)={}".format(dir(f)))
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    response = HttpResponse(template.render({'flatpage': f}, request))
    return response
