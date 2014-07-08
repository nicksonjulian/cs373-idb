from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Put list of countries here or something")

def detail(request, country_id):
    return HttpResponse("You're looking at country %s." % country_id)
