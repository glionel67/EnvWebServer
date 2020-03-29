FROM raspbian:stretch #raspbian:jessie

MAINTAINER Lionel <lionel.geneve@gmail.com>

RUN sudo apt update
RUN sudo apt upgrade
RUN sudo apt update

# General
RUN sudo apt install -y i2c-tools git build-essential

# Database
RUN sudo apt install -y sqlite3

# Apache web server + PHP
RUN sudo apt install -y apache2 php php-mbstring php-mysql libapache2-mod-php

# Samba server
RUN sudo apt install -y samba samba-common-bin
# Help/config: https://raspberry-pi.fr/raspberry-pi-nas-samba/, https://www.framboise314.fr/partager-un-repertoire-sous-jessie-avec-samba/

# Docker
# Help: https://www.docker.com/blog/happy-pi-day-docker-raspberry-pi/
# Help: https://linuxize.com/post/how-to-install-and-use-docker-on-raspberry-pi/
#RUN sudo apt remove docker docker-engine docker.io containerd runc
RUN sudo apt install -y apt-transport-https ca-certificates software-properties-common
RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
RUN sudo usermod -aG docker $USER

# Stream video via html
sudo apt install -y motion

# Python
RUN sudo apt install -y python python-dev python-pip python-picamera python-numpy 
RUN sudo apt install -y python3 python3-dev python3-pip python3-picamera python3-numpy
RUN sudo apt install -y python-smbus python-mysqldb
RUN sudo apt install -y python-gpiozero python3-gpiozero python-pigpio python3-pigpio
RUN python -m pip install Django
RUN python3 -m pip install Django
RUN python -m pip install plotly==4.5.2
RUN python3 -m pip install plotly==4.5.2

# Time/ntp
RUN sudo apt install ntp
RUN sudo systemctl enable ntp
RUN sudo timedatectl set-ntp 1