<div align="center">
  <h1> Trabalho 5 - Python + Mosquitto</h1>
  <p>Esse projeto foi desenvolvido durante a disciplina de Sistemas Distribuidos e tem como objetivo criar uma aplicação que simule a leitura de um sensor enviando dados a um broker ao mesmo tempo que solicita os dados desse mesmo broker. </p>
</div>

## Tecnologias Utilizadas 🛠️
Este projeto foi criado usando as seguintes tecnologias
- [Python3](https://www.python.org)
- [Paho-Mqtt](https://pypi.org/project/paho-mqtt/)


## Como utilizar esse projeto 📦

1. Instalar o broker Mosquitto:
	sudo apt-get install mosquitto
	sudo apt-get install mosquitto-clients

2. Instalar o Python, caso não tenha instalado:
	sudo apt-get install python3

3. Instalar o pip, caso não tenha instalado:
	sudo apt install python3-pip

4. Instalar a biblioteca do Mosquitto para Python:
	pip install paho-mqtt

Para o Publish:
	Executar o arquivo:

		python Publish.py

	Informar o IP da maquina onde o broker vai rodar (127.0.0.1)

	Informar o cômodo que vai ser simulado

Para o Subscribe:

	Executar o arquivo:

		python Subscribe.py

	Informar o IP da maquina onde o broker vai rodar (127.0.0.1)

