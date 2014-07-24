from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Athlete

def index(request):
    return HttpResponse("Put list of athletes here or something")

def detail(request, athlete_id):
    name = athlete_id.split("_")
    f_name = name[0].capitalize()
    l_name = name[1].capitalize()
    athlete = Athlete.objects.get(first_name=f_name)
    context = {'athlete': athlete}
    return render(request, 'athlete/dynamic_athlete.html', context)
