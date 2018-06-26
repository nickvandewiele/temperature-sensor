# Sensor - Data Collector setup running on RPI and PC

## Introduction

This repo provides the code for a temperature sensor (Adafruit MCP9808) that is measuring data and sending it over the General Purpose Input/Output (GPIO) pins of a Raspberry Pi 3 (RPI). The measured data is collected by another machine, and stored in a MySQL database for further use.

The sensor - collector setup is designed using the following microservices:
1. a sensor service that accesses the sensor and runs on the RPI.
2. a collector service that collects the data emitted by the sensor service and subsequently stores it in a database. This service runs on a remote host, e.g. your PC.
3. a client that periodically instructs the collector service to collect data, also running on a remote host, e.g. your PC.

Communication between the services occurs via HTTP requests over the network.


## Setting up the Adafruit MCP9808 sensor

4 pins of the MCP9808 sensor are needed:
- power pin (VDD)
- ground pin (GND)
- I2C SDA (Serial Data Line) pin
- I2C SCL (Serial Clock Line) pin

Connect them to the corresponding pins of the GPIO on your RPI.


## Setting up the RPI

The RPI is running the NOOBS OS.

Since the sensor measurements flow through the I2C bus of the RPI, it needs to be activated first. Enabling I2C support on RPI can be done through `raspi-config`.

Make sure the following two modules are loaded at start-up, and are found in `/etc/modules`:
`
i2c-bcm2708
i2c-dev
`

Verify if the I2C bus has addresses in use:
`i2cdetect 1`

## Setting up a database server

Install MySQL server and run it as a service. Make sure you have the following databases available on your MySQL server:
- temperature_dev (development)
- temperature_test (testing)
- temperature_prod (production)

See `create.sql` for an example script.

## Microservices

### Sensor service

The sensor service is a python Flask application that needs to be started on port 5001 on the RPI.

First, on the RPI, install the dependencies of the sensor service:
`pip install -r app/services/sensor/requirements.txt`

requirements.txt contains the Adafruit MCP9808 sensor wrappers for Python, and refers to the Adafruit Python GPIO wrapper in its own dependencies.

Next run the flask server on port 5001:
`python app/services/sensor/manage.py -h 0.0.0.0 -p 5001`

Tests can be run as follows:
`python app/services/sensor/manage.py test`

### Collector service, Client

The Collector service and client are defined as Docker containers, and can be spun-up
through a docker-compose script:

`docker-compose -f docker-compose-dev.yml up -d --build`

Make sure you add the following:
- IP address of the machine running the database server
- IP address of the RPI running the sensor

Tests can be run as follows:
`docker-compose -f docker-compose-dev.yml run collector python manage.py test`

The collector service is another python Flask service.
Data is written to the database table via the Object Relational Mapper of sql-alchemy.


## Useful Links
- https://aaronkuehler.com/blog/2014/12/01/raspberry-pi-temperature-sensor/
- https://learn.adafruit.com/adafruit-mcp9808-precision-i2c-temperature-sensor-guide/overview