FROM python:3.9.5

RUN apt-get update
RUN apt-get --quiet install fluidsynth --yes
RUN pip install midi2audio
