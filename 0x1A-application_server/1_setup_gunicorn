#!/usr/bin/env bash
# Script to set up production environment with Gunicorn

# Install Gunicorn and other required libraries
sudo pip3 install gunicorn

# Start Gunicorn and bind it to port 5000
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app

