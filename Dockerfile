# Dockerfile
FROM python:3.9-alpine

# Install nginx
RUN apk add --no-cache nginx

# Copy the nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the Python script
COPY server.py /usr/local/bin/server.py

# Copy the startup script
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

# Expose the port
EXPOSE 80

# Start nginx and the Python script
CMD ["sh", "/usr/local/bin/start.sh"]
