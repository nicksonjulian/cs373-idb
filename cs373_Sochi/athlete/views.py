from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Put list of athletes here or something")

def detail(request, athlete_id):
    return HttpResponse("You're looking at athlete %s." % athlete_id)

def ireen(request):
    return render_to_response('athlete/ireenwust.html')

def tobias(request):
    return render_to_response('athlete/tobiasarlt.html')
