#!/bin/bash
# Script used to run the EnvWebServer
#echo "EnvWebServer will be started..."
python3 ../manage.py runserver 0.0.0.0:8001 #&
#echo "EnvWebServer started!"