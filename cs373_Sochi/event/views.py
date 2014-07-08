from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Put list of events here or something")

def detail(request, event_id):
    return HttpResponse("You're looking at event %s." % event_id)

