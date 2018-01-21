from django.http.response import HttpResponse
from django.views.generic import View
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Post

"""
def post_list(request):
    post_list = Post.objects.all()
    template = loader.get_template('blog/post_list.html')
    output = template.render({'post_list': post_list})
    return HttpResponse(output)
"""

class PostList(View):

    def get(self, request):
        post_list = Post.objects.all()
        template = loader.get_template('blog/post_list.html')
        output = template.render({'post_list': post_list})
        return HttpResponse(output)

def post_detail(request, year, month, slug):
    post = get_object_or_404(Post,
                             pub_date__year=year,
                             pub_date__month=month,
                             slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
