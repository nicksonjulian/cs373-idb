from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render

from home.models import Events

def index(request):
    events = Events.objects.all()
    context = {'events': events}
    return render(request, 'event/eventlist.html', context)

def detail(request, sport_name, event_name):
    event_name = event_name.replace("_", " ").title()
    event_name = event_name.replace("ies", "ies'").replace("ns", "n's")

    try:
        event = Events.objects.get(name=event_name)
        context = {'event': event}
    except Events.DoesNotExist:
        raise Http404
    return render(request, 'event/dynamic_event.html', context)