from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render

from home.models import Country

def index(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'country/countrylist.html', context)

def detail(request, country_id):
    country_name = country_id.replace("_", " ").title()

    try:
        country = Country.objects.get(name=country_name)
        context = {'country': country}
    except Country.DoesNotExist:
        raise Http404

    return render(request, 'country/dynamic_country.html', context)