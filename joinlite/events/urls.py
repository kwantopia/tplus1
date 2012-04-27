from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',

    # post
    url(r'^configure/$', 'configure', name='event_configure'),

    # post/get
    url(r'^login/$', 'login', name='event_login'),

    # get
    url(r'^logout/$', 'logout', name='event_logout'),

    # get
    url(r'^start/$', 'start', name='event_start'),

    url(r'^round/start/$', 'start_round', name='start_round'),
    url(r'^round/pause/$', 'pause_round', name='pause_round'),
    url(r'^round/end/$', 'end_round', name='end_round'),
    url(r'^round/restart/$', 'restart_round', name='restart_round'),

    # post 
    url(r'^topic/add/$', 'add_topic', name='add_topic'),
    url(r'^topic/del/$', 'del_topic', name='del_topic'),
    url(r'^round/duration/set/$', 'set_round_duration', name='set_round_duration'),
    url(r'^user/add/$', 'add_user', name='add_user'),
    url(r'^user/update/$', 'update_user', name='update_user'),
    url(r'^user/del/$', 'del_user', name='del_user'),
    url(r'^survey/completed/$', 'survey_completed', name='survey_completed'),
)
