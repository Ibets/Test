FROM python:3.7-stretch 

WORKDIR /app

COPY flask_server.py ./
COPY haarcascade_frontalface_default.xml ./

RUN apt update
RUN apt install -y libglu1
RUN pip3 install Flask
RUN pip3 install numpy
RUN pip3 install jsonpickle
RUN pip3 install opencv-python

EXPOSE 5000

CMD ["python3", "flask_server.py"]