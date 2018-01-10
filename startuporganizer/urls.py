"""startuporganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from organizer.views import homepage, tag_detail, startup_detail, startup_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ex: /
    url(r'^$', homepage, name='homepage'),
    # ex: /tag/djagno-web
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    # ex: /startup
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    # ex: /startup/google
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
]
