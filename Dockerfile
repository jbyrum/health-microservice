#Grab the latest alpine image
FROM python:3.6-slim

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
