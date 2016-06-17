from django.contrib.syndication.views import Feed
from vblog.models import Entry

class LatestPosts(Feed):
    title = "My Video blog"
    link = "/feed/"
    description = "latest posts"
    
    def items(self):
        return Entry.objects.published()[:5]