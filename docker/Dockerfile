FROM python:3.8-slim-buster

MAINTAINER Yury Antonov <yantonov@yandex.ru>

RUN pip install --upgrade pip
ADD files/* /root/
RUN pip install -r /root/requirements.txt

WORKDIR /src

ENTRYPOINT [ "/root/init.sh" ]
