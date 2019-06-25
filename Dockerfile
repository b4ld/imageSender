FROM python:3.7.3-stretch


RUN sudo pip3 install Flask
RUN sudo pip3 install requests


CMD ["python3", "server.py"]