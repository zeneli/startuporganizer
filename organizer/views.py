from django.http.response import HttpResponse
from django.template import loader

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template(
        'organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)

def tag_detail(request, slug):
    template = loader.get_template('organizer/tag_detail.html')
    output = template.render()
    return HttpResponse(output)
