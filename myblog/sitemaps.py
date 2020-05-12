from django.contrib.sitemaps import Sitemap
from .models import post

class postSiteMap(Sitemap):
    changefreq='daily'
    priority='0.9'

    def items(self):
        return post.published_posts.all()

    def lastmod(self,obj):
        return obj.updated
