from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Events

def index(request):
    return HttpResponse("Select an event.")

def ldoubles(request):
    return render_to_response('event/l-doubles.html')

def fsicedancefreedance(request):
    return render_to_response('event/fs-icedancefreedance.html')

def ssladies3000m(request):
    return render_to_response('event/ss-ladies3000m.html')

def detail(request, event_id):
    if (event_id == "luge_luge_doubles"):
        event = Events.objects.get(name="Luge Doubles")
        context = {'event': event, 'icon': "/static/athlete/images/l_icon.png"}
        return render(request, 'event/dynamic_event.html', context)
    elif (event_id == "figure_skating_ice_dance_free_dance"):
        event = Events.objects.get(name="Ice Dance Free Dance")
        context = {'event': event, 'icon': "/static/athlete/images/fs_icon.png"}
        return render(request, 'event/dynamic_event.html', context)
    elif (event_id == "2"):
        event = Events.objects.get(name="speed_skating_ladies_3000m")
        context = {'event': event, 'icon': "/static/athlete/images/ss_icon.png"}
        return render(request, 'event/dynamic_event.html', context)
    else:
        return HttpResponse("You're looking at event %s." % event_id)