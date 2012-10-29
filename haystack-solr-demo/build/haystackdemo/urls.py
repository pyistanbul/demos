from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Search
    url(r'^search/', include('haystack.urls')),

    # Articles
    url(r'^articles/', include('articles.urls')),
)

urlpatterns += patterns('django.views.generic.simple',
    # Home
    url(r'^$', 'direct_to_template', {
        'template': 'home.html',
    }, name='home'),
    
)
