#!/usr/bin/env bash
# sets up Airbnb static_web files amd folders
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo "Airbnb Project" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown ubuntu:ubuntu -hR /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
