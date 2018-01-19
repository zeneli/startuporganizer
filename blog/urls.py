from django.conf.urls import url
from .views import PostList


urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog_post_list'),
]
