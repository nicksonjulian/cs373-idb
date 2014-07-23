from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Athlete

def index(request):
    return HttpResponse("Put list of athletes here or something")

def detail(request, athlete_id):
    if (athlete_id == "0"):
        athlete = Athlete.objects.get(first_name="Ireen")
        context = {'athlete': athlete, 'picture': "/static/athlete/images/ireenwust.jpg", 'flag': "/static/athlete/images/ned.png", 'video': "https://www.youtube.com/v/50H_s-89ckU"}
        return render(request, 'athlete/dynamic_athlete.html', context)
    elif (athlete_id == "1"):
        athlete = Athlete.objects.get(first_name="Meryl")
        context = {'athlete': athlete, 'picture': "/static/athlete/images/meryldavis.png", 'flag': "/static/athlete/images/usa.png", 'video': "https://www.youtube.com/v/w9yX3S9VdtI"}
        return render(request, 'athlete/dynamic_athlete.html', context)
    elif (athlete_id == "2"):
        athlete = Athlete.objects.get(first_name="Tobias")
        context = {'athlete': athlete, 'picture': "/static/athlete/images/tobiasarlt.png", 'flag': "/static/athlete/images/ger.png", 'video': "https://www.youtube.com/v/zpzMtBK-yOA"}
        return render(request, 'athlete/dynamic_athlete.html', context)
    else:
        return HttpResponse("You're looking at athlete %s." % athlete_id)

def ireen(request):
    return render_to_response('athlete/ireenwust.html')

def tobias(request):
    return render_to_response('athlete/tobiasarlt.html')

def meryl(request):
    return render_to_response('athlete/meryldavis.html')

