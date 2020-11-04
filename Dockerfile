FROM python:3.8
ADD ./requirements.txt .
RUN mkdir ./src
ADD ./src /src
RUN pip3 install -r requirements.txt
WORKDIR /src/dockerlesson