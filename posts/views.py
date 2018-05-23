from django.shortcuts import render
from django.core import serializers
from . models import feed
import json

# Create your views here.

def index(request):
    template="posts/index.html"
    results=feed.objects.all()
    context={
        'results':results,
    }
    print ("hiii")
    return render(request,template,context)

def baselayout(request):
    template="posts/base.html"
    return render(request,template)

def errorpage(request):
    template="posts/error.html"
    return render(request,template)