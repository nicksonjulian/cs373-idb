from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from home.models import Country

def index(request):
    return HttpResponse("Search for a specific country.")

def detail(request, country_id):
        country_name = country_id.replace("_", " ").title()
        country = Country.objects.get(name=country_name)
        context = {'country': country}
        return render(request, 'country/dynamic_country.html', context)