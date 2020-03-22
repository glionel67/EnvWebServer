raspbian/stretch #raspbian/jessie


sudo apt update
sudo apt upgrade
sudo apt update

# General
sudo apt install -y i2c-tools git build-essential

# Database
sudo apt install -y sqlite3

# Apache web server + PHP
sudo apt install -y apache2 php php-mbstring php-mysql libapache2-mod-php

# Samba server
sudo apt install -y samba samba-common-bin
# Help/config: https://raspberry-pi.fr/raspberry-pi-nas-samba/, https://www.framboise314.fr/partager-un-repertoire-sous-jessie-avec-samba/

# Docker
# Help: https://www.docker.com/blog/happy-pi-day-docker-raspberry-pi/
# Help: https://linuxize.com/post/how-to-install-and-use-docker-on-raspberry-pi/
#sudo apt remove docker docker-engine docker.io containerd runc
sudo apt install -y apt-transport-https ca-certificates software-properties-common
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER

# Python
sudo apt install -y python python-dev python-pip python-picamera python-numpy 
sudo apt install -y python3 python3-dev python3-pip python3-picamera python3-numpy
sudo apt install -y python-smbus python-mysqldb
sudo apt install -y python-gpiozero python3-gpiozero python-pigpio python3-pigpio
python -m pip install Django
python -m pip install plotly==4.5.2

# Time/ntp
sudo apt install ntp
sudo systemctl enable ntp
sudo timedatectl set-ntp 1