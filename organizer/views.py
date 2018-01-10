from django.http.response import HttpResponse
from django.template import loader

from .models import Tag, Startup


def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template(
        'organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    template = loader.get_template('organizer/tag_detail.html')
    output = template.render({'tag': tag})
    return HttpResponse(output)

def startup_detail(request, slug):
    startup = Startup.objects.get(slug__iexact=slug)
    template = loader.get_template('organizer/startup_detail.html')
    output = template.render({'startup': startup})
    return HttpResponse(output)
