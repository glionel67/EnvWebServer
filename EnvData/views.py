from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import json

import sys
sys.path.append("../Tools")
from Tools.plotDatabase import plotDatabase
from Tools.queryDatabase import queryDatabase
from Tools.getDataBme280 import getDataBme280

import random
from datetime import datetime

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
    data = []
    if duration == "none":
        #print("Not implemented: none")
        pass
    elif duration == "all":
        #print("all")
        # Get plot HTML code
        data = queryDatabase("envData.db", "all")
        #div, fig = plotDatabase(data)
    elif duration == "day":
        data = queryDatabase("envData.db", "lastDay")
        #div, fig = plotDatabase(data)
    elif duration == "week":
        data = queryDatabase("envData.db", "lastWeek")
        #div, fig = plotDatabase(data)
    elif duration == "month":
        data = queryDatabase("envData.db", "lastMonth")
        #div, fig = plotDatabase(data)
    elif duration == "year":
        data = queryDatabase("envData.db", "lastYear")
        #div, fig = plotDatabase(data)
    else:
        pass

    temperatureTable = list()
    humidityTable = list()
    pressureTable = list()
    for i, row in enumerate(data):
        t = float(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").strftime('%s')) * 1000
        temperatureTable.append([t, row[1]])
        humidityTable.append([t, row[2]])
        pressureTable.append([t, row[3]])

    context = {'div': div, \
    'temperatureTable' : json.dumps(temperatureTable), \
    'humidityTable' : json.dumps(humidityTable), \
    'pressureTable' : json.dumps(pressureTable)}
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
    temperature, humidity, pressure = 0.0, 0.0, 0.0
    try:
        temperature, humidity, pressure = getDataBme280()
    except:
        print("Getting real data failed, using random values...")
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