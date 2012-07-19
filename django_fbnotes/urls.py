from django.conf.urls import patterns, include, url
from fbnotes.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_fbnotes.views.home', name='home'),
    # url(r'^django_fbnotes/', include('django_fbnotes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^save$', save),
    url(r'^note$', note),
    url(r'^logout$', logout),
    url(r'', include('social_auth.urls')),
)
