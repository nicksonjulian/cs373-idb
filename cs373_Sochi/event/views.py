from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Select an event.")

def detail(request, event_id):
    return HttpResponse("You're looking at athlete %s." % athlete_id)

def ldoubles(request):
    return render_to_response('event/l-doubles.html')

def fsicedancefreedance(request):
    return render_to_response('event/fs-icedancefreedance.html')

def ssladies3000m(request):
    return render_to_response('event/ss-ladies3000m.html')

