from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

try:
    import gpiozero
except:
    print("Failed to import gpiozero library")

# GPIO pin BCM numeros (ev1, ev2, ev3, ev4, pump)
# Ev1 = 22
# Ev2 = 23
# Ev3 = 24
# Ev4 = 25
# Pump = 27
gpios = [None] * 5
try:
    gpios = [gpiozero.LED(22), gpiozero.LED(23), gpiozero.LED(24), \
    gpiozero.LED(25), gpiozero.LED(27)]
except:
    print("Failed to initialize the GPIOs")

# GPIO pin states: 1 = "ON", 0 = "OFF"
pinStates = ["OFF", "OFF", "OFF", "OFF", "OFF"]

def index(request):
    """index function"""
    global gpios
    global pinStates

    # Check RPi pin states to update these values
    for i, gpio in enumerate(gpios):
        val = gpio.value
        if val == 0:
            pinStates[i] = "OFF"
        else:
            pinStates[i] = "ON"

    # Set context
    context = {'ev1State' : pinStates[0], 'ev2State' : pinStates[1], \
    'ev3State' : pinStates[2], 'ev4State' : pinStates[3], \
    'pumpState' : pinStates[4]}
    # Return HTML page with plot
    return render(request, "Control/index.html", context)

def action(request, action):
    """action function"""
    global gpios
    global pinStates

    #print("action={}".format(action))

    # Turn on/off the state of the GPIO
    if action == "ev1On":
        val = gpios[0].on()
    elif action == "ev1Off":
        val = gpios[0].off()
    elif action == "ev2On":
        val = gpios[1].on()
    elif action == "ev2Off":
        val = gpios[1].off()
    elif action == "ev3On":
        val = gpios[2].on()
    elif action == "ev3Off":
        val = gpios[2].off()
    elif action == "ev4On":
        val = gpios[3].on()
    elif action == "ev4Off":
        val = gpios[3].off()
    elif action == "pumpOn":
        val = gpios[4].on()
    elif action == "pumpOff":
        val = gpios[4].off()
    else:
        print("Invalid action")

    # Check RPi pin states to update these values
    for i, gpio in enumerate(gpios):
        val = gpio.value
        if val == 0:
            pinStates[i] = "OFF"
        else:
            pinStates[i] = "ON"
        print("Pin idx {}: state={}".format(i, pinStates[i]))

    # Set context
    context = {'ev1State' : pinStates[0], 'ev2State' : pinStates[1], \
    'ev3State' : pinStates[2], 'ev4State' : pinStates[3], \
    'pumpState' : pinStates[4]}

    # Return HTML page with plot
    return render(request, "Control/index.html", context)
