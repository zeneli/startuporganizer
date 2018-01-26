from django.conf.urls import url

from .views import (
    homepage, tag_create, tag_list, tag_detail,
    startup_detail, startup_list)



urlpatterns = [
    # ex: /
    url(r'^$', homepage, name='homepage'),
    # ex: /tag/create/
    url(r'^tag/create/$', tag_create, name='organizer_tag_create'),
    # ex: /tag/
    url(r'^tag/$', tag_list, name='organizer_tag_list'),
    # ex: /tag/djagno-web
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    # ex: /startup
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    # ex: /startup/google
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
]
