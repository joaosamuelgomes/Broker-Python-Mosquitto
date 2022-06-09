FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install net-tools
RUN apt-get -y install iputils-ping
RUN apt-get -y install mosquitto
RUN apt-get -y install mosquitto-clients

EXPOSE 1883


