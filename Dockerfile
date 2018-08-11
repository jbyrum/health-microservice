#Grab the latest alpine image
#FROM heroku/heroku:16
FROM python:3.6-slim

# Heroku-16 Install python and pip
#RUN apt-get update && apt-get install -y python3-pip

ADD requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install -r /tmp/requirements.txt

# Add our code
ADD . /opt/webapp/
WORKDIR /opt/webapp

# Heroku-16 Run the image as a non-root user
RUN useradd -m myuser
USER myuser

# Run the app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi --reload
