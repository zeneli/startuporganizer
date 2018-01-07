from django.http.response import HttpResponse


def homepage(request):
    return HttpResponse('Hello World!')
