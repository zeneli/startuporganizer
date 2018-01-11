from django.conf.urls import url

from .views import homepage, tag_detail, startup_detail, startup_list


urlpatterns = [
    # ex: /
    url(r'^$', homepage, name='homepage'),
    # ex: /tag/djagno-web
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    # ex: /startup
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    # ex: /startup/google
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
]
