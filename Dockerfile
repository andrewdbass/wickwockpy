FROM python:3.5

ENV CPATH=/usr/local/include/python3.5m

RUN mkdir /wickwockpy
WORKDIR /wickwockpy

ADD requirements.txt /wickwockpy/requirements.txt
RUN pip install --no-cache-dir --src /usr/src -r requirements.txt

ADD . /wickwockpy
