from django.http.response import HttpResponse
from django.template import loader

from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    template = loader.get_template('blog/post_list.html')
    output = template.render({'post_list': post_list})
    return HttpResponse(output)
