from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import events

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'events.views.home', name='home'),
    # url(r'^joinlite/', include('joinlite.foo.urls')),

    url(r'^about/$', 'main.views.about', name='about'),
    url(r'^team/$', 'main.views.team', name='team'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),
)
