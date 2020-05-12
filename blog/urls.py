
from django.contrib import admin
from django.urls import path,include
from myblog import views
from myblog.sitemaps import postSiteMap
from django.contrib.sitemaps.views import sitemap

sitemaps={'post':postSiteMap,}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    path('blog/', include('myblog.urls')),
    path('sitemap.xml', sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
