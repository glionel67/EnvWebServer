from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#from file import function

import sys
sys.path.append("../Tools")
from Tools.plotDatabase import plotDatabase

def index(request):
    """index function"""
    # Load HTML page template
    template = loader.get_template("EnvData/index.html")
    context = {}
    # Return HTML page with plot
    return render(request, "EnvData/index.html", context)

def display(request):
    """display function"""
    # Get plot HTML code
    div, fig = plotDatabase()
    # Load HTML page template
    template = loader.get_template("EnvData/display.html")
    context = {'div': div}
    # Return HTML page with plot
    return render(request, "EnvData/display.html", context)