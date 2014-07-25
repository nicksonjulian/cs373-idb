from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render

from home.models import Athlete

def index(request):
    athletes = Athlete.objects.all()
    context = {'athletes': athletes}
    return render(request, 'athlete/athletelist.html', context)

def detail(request, athlete_id):
    name = athlete_id.split("_")
    f_name = name[0].capitalize()
    l_name = name[1].capitalize()

    try:
        athlete = Athlete.objects.get(first_name=f_name)
        context = {'athlete': athlete}
    except Athlete.DoesNotExist:
        raise Http404

    return render(request, 'athlete/dynamic_athlete.html', context)
