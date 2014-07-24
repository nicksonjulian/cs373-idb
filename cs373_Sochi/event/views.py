from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Events

def index(request):
    return HttpResponse("Select an event.")

def detail(request, sport_name, event_name):
    event_name = event_name.replace("_", " ").title()
    event_name = event_name.replace("ies", "ies'").replace("ns", "n's")
    event = Events.objects.get(name=event_name)
    context = {'event': event}
    return render(request, 'event/dynamic_event.html', context)