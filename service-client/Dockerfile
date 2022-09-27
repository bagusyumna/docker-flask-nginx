# Use the Python:3.8.2 container image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
# CMD ["uwsgi", 'app.ini']