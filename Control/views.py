from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# TODO: pap these values to the real states of the RPi IOs
pumpState = "OFF" # "ON"/"OFF"
ev1State = "OFF" # "ON"/"OFF"
ev2State = "OFF" # "ON"/"OFF"

def index(request):
    """index function"""
    global pumpState
    global ev1State
    global ev2State

    # TODO: check RPi pin state to update these values
    # ...

    # Get HTML template
    #template = loader.get_template("Control/index.html")
    context = {'pumpState' : pumpState, 'ev1State' : ev1State, \
    'ev2State' : ev2State}
    # Return HTML page with plot
    return render(request, "Control/index.html", context)

def action(request, action):
    """pumpOnClick function"""
    global pumpState
    global ev1State
    global ev2State

    #print("action={}".format(action))

    # TODO: turn on/off the state of the actual IO
    if action == "pumpOn":
        pumpState = "ON"
    elif action == "pumpOff":
        pumpState = "OFF"
    elif action == "ev1On":
        ev1State = "ON"
    elif action == "ev1Off":
        ev1State = "OFF"
    elif action == "ev2On":
        ev2State = "ON"
    elif action == "ev2Off":
        ev2State = "OFF"

    #print("pumpState={}, ev1State={}, ev2State={}".format(pumpState, ev1State, ev2State))

    # Get HTML template
    #template = loader.get_template("Control/index.html")
    context = {'pumpState' : pumpState, 'ev1State' : ev1State, \
    'ev2State' : ev2State}
    # Return HTML page with plot
    return render(request, "Control/index.html", context)