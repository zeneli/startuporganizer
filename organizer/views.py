from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .models import Tag, Startup
from .forms import TagForm


def homepage(request):
    template = loader.get_template('organizer/homepage.html')
    output = template.render({})
    return HttpResponse(output)

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
    else:  # request.method != 'POST'
        form = TagForm()
    return render(request, 'organizer/tag_form.html', {'form': form})

def tag_list(request):
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

def startup_list(request):
    startup_list = Startup.objects.all()
    template = loader.get_template('organizer/startup_list.html')
    output = template.render({'startup_list': startup_list})
    return HttpResponse(output)

def startup_detail(request, slug):
    startup = Startup.objects.get(slug__iexact=slug)
    template = loader.get_template('organizer/startup_detail.html')
    output = template.render({'startup': startup})
    return HttpResponse(output)
