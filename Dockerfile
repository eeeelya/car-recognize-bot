FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -r requirements.txt
RUN pip install onnxruntime
