from django.http.response import HttpResponse
from django.template import Context, loader

from .models import Tag, Startup # ! without .
from django.shortcuts import render

def homepage(request):
    return render(request, 'organizer/homepage.html')

def tag_list(request):
    tag_list = Tag.objects.all()
    context = {'tag_list': tag_list}
    return render(request, 'organizer/tag_list.html', context)

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    context = {'tag': tag}
    return render(request, 'organizer/tag_detail.html', context)

def startup_list(request):
    startup_list = Startup.objects.all()
    context = {'startup_list': startup_list}
    return render(request, 'organizer/startup_list.html', context)

def startup_detail(request, slug):
    startup = Startup.objects.get(slug__iexact=slug)
    context = {'startup': startup}
    return render(request, 'organizer/startup_detail.html', context)