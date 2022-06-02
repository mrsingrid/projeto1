from django.http import HttpResponse


def home(request):
    return HttpResponse('home 1')
