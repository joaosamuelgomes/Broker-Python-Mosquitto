FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install net-tools
RUN apt-get -y install iputils-ping
RUN apt-get -y install mosquitto
RUN apt-get -y install mosquitto-clients
RUN groupadd -g 1883 mosquitto && \  
	useradd -r -u 1883 -g mosquitto mosquitto

EXPOSE 1883/udp

CMD [ "/usr/sbin/mosquitto", "-c", "/mosquitto/config/mosquitto.conf]

