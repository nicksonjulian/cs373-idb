from django.shortcuts import render

from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('home/home.html')
