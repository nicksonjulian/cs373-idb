from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Search for a specific country.")

def usa(request):
    return render_to_response('country/usa.html')

def ger(request):
    return render_to_response('country/ger.html')

def ned(request):
    return render_to_response('country/ned.html')
