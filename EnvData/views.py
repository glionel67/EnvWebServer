from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from file import function

import sys
sys.path.append("../Tools")
from plotDatabase import plotDatabase

def index(request):
    """index function"""
    #return HttpResponse("Hello, world. You're at the EnvData index.")
    div, fig = plotDatabase()
    template = loader.get_template('EnvData/index.html')
    context = {'div': div}
    #return HttpResponse(div)
    return render(request, "EnvData/index.html", context)