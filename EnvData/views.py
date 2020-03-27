from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import random

import sys
sys.path.append("../Tools")
from Tools.plotDatabase import plotDatabase

def index(request):
    """index function"""
    # Load HTML page template
    #template = loader.get_template("EnvData/index.html")
    context = {}
    # Return HTML page with plot
    return render(request, "EnvData/index.html", context)

def display(request, duration):
    """display function"""

    #print("duration={}".format(duration))

    div = ""
    fig = None
    if duration == "none":
        #print("Not implemented: none")
        pass
    elif duration == "all":
        #print("all")
        # Get plot HTML code
        div, fig = plotDatabase()
    elif duration == "day":
        #print("Not implemented: day")
        pass
    elif duration == "week":
        #print("Not implemented: week")
        pass
    elif duration == "month":
        #print("Not implemented: month")
        pass
    elif duration == "year":
        #print("Not implemented: year")
        pass
    elif duration == "realtime":
        pass
    else:
        pass

    # Load HTML page template
    #template = loader.get_template("EnvData/display.html")
    context = {'div': div}
    # Return HTML page with plot
    return render(request, "EnvData/display.html", context)

def realtime(request):
    """realtime function"""
    # Load HTML page template
    context = {}
    # Return HTML page with plot
    return render(request, "EnvData/realtime.html", context)

def update(request):
    """update function"""
    temperature = str(random.gauss(21, 10))
    humidity = str(random.gauss(50, 10))
    pressure = str(random.gauss(1010, 10))
    s = str(temperature) + ";" + str(humidity) + ";" + str(pressure)
    return HttpResponse(s , status=200)

def temperature(request):
    """temperature function"""
    temperature = str(random.gauss(21, 10))
    return HttpResponse(temperature, status=200)

def humidity(request):
    """humidity function"""
    humidity = str(random.gauss(50, 10))
    return HttpResponse(humidity, status=200)

def pressure(request):
    """pressure function"""
    pressure = str(random.gauss(1010, 10))
    return HttpResponse(pressure, status=200)