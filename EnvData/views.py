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
    else:
        pass

    # Load HTML page template
    #template = loader.get_template("EnvData/display.html")
    context = {'div': div}
    # Return HTML page with plot
    return render(request, "EnvData/display.html", context)