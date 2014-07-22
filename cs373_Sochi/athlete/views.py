from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Athlete

def index(request):
    return HttpResponse("Put list of athletes here or something")

def detail(request, athlete_id):
    if (athlete_id == "0"):
        athlete = Athlete.objects.get(first_name="Ireen")
        context = {'athlete': athlete}
        return render(request, 'athlete/dynamic_athlete.html', context)
    elif (athlete_id == "1"):
        athlete = Athlete.objects.get(first_name="Meryl")
        context = {'athlete': athlete}
        return render(request, 'athlete/dynamic_athlete.html', context)
    elif (athlete_id == "2"):
        athlete = Athlete.objects.get(first_name="Tobias")
        context = {'athlete': athlete}
        return render(request, 'athlete/dynamic_athlete.html', context)
    else:
        return HttpResponse("You're looking at athlete %s." % athlete_id)

def ireen(request):
    return render_to_response('athlete/ireenwust.html')

def tobias(request):
    return render_to_response('athlete/tobiasarlt.html')

def meryl(request):
    return render_to_response('athlete/meryldavis.html')

