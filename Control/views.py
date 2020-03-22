from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    """index function"""
    if request.method == 'POST':
        if 'pumpOn' in request.POST:
            print("PUMP ON")
        elif 'pumpOff' in request.POST:
            print("PUMP OFF")
    # Get HTML template
    template = loader.get_template("Control/index.html")
    context = {}
    # Return HTML page with plot
    return render(request, "Control/index.html", context)
