#!/bin/sh

# Start nginx in the background
nginx &

# Start the Python server
python /usr/local/bin/server.py
