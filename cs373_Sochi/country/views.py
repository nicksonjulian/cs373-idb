from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Country

def index(request):
    return HttpResponse("Search for a specific country.")

def usa(request):
    return render_to_response('country/usa.html')

def ger(request):
    return render_to_response('country/ger.html')

def ned(request):
    return render_to_response('country/ned.html')

def detail(request, country_id):
    if (country_id == "0"):
        country = Country.objects.get(name="Germany")
        context = {'country': country, 'flag': "/static/athlete/images/ger.png"}
        return render(request, 'country/dynamic_country.html', context)
    elif (country_id == "1"):
        country = Country.objects.get(name="United States")
        context = {'country': country, 'flag': "/static/athlete/images/usa.png"}
        return render(request, 'country/dynamic_country.html', context)
    elif (country_id == "2"):
        country = Country.objects.get(name="Netherlands")
        context = {'country': country, 'flag': "/static/athlete/images/ned.png"}
        return render(request, 'country/dynamic_country.html', context)
    else:
        return HttpResponse("You're looking at country %s." % country_id)