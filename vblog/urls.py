"""vblog app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views, feed
#from django.contrib.flatpages import views as flatviews

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.VBlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.VBlogDetail.as_view(), name="entry_detail"),
    url(r'^event/(?P<slug>\S+)$', views.EventDetail.as_view(), name="event_detail"),
    #url(r'^about/$', flatviews.flatpage, {'url': '/about/'}, name='about'),
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name="about_detail"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
