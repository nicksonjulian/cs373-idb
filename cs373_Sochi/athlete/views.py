from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Put list of athletes here or something")

def detail(request, athlete_id):
    return HttpResponse("You're looking at athlete %s." % athlete_id)
