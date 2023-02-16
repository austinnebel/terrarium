# Climate Controller

## Overview

This repository uses a Raspberry Pi Zero W to control and monitor the climate of a given environment. It includes a python-implemented embedded system, a React frontend, and a Django backend that implements both HTTP and WebSocket connections.

The Raspberry Pi will continuously read temperature and humidity information from a DHT22 sensor and publish that information to a websocket on the Django backend. The React frontend can connect to that websocket to read information in real time, and can publish GET requests to certain endpoints to receive past data over a specified period of time.

Below is a screenshot of the frontend application when the project is running:

<div style="display: flex; max-height: 500px; justify-content: center;">
    <img src="./docs/Climate-screenshot-1.png" alt="screenshot-1" style="object-fit: contain"/>
    <img src="./docs/Climate-screenshot-2.png" alt="screenshot-2"style="object-fit: contain"/>
</div>

### Embedded Components

> **NOTE**
> The documentation for the embedded project can be found [here](embedded/README.md).

The embedded project is designed to work with a Raspberry Pi Zero W, DHT22 sensor, GPIO relay, humidifier, heat lamp, and heating pad. The DHT22 sensor captures humidity and temperature data, and the GPIO relay provides or cuts power from the heat lamp, humidifier, and heating pad. The software in the embedded project takes the running average of readings from the DHT22 and uses the results to determine what devices to turn on or off. The project will also push this data to a websocket in the backend project and store data in the backend database.

### Django Backend

> **NOTE**
> The documentation for the backend can be found [here](backend/README.md).

The `embedded` package periodically pushes climate information to the backend. This data can both be saved in the database as well as published to a websocket. The websocket can be used to broadcast real-time data without bloating the database, while saving data to the database allows for reading past information over a period of time. The websocket channels in Django are implemented by connecting to a [redis](https://redis.io/docs/getting-started/) instance.

### React Frontend

> **NOTE**
> The documentation for the frontend can be found [here](frontend/README.md).

The frontend service is designed to display real-time information about the climate data captured by the DHT22 sensor in the `embedded` project. It displays temperature and humidity data, along with two graphs display the history of each.

## Installation

### Dev Requirements

-   [docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

### Deploy Requirements

These must be installed on the Raspberry Pi to deploy the project.

-   Python 3.9
-   `pipenv`
    -   `sudo -H pip install -U pipenv`
-   `redis-server`
-   [Adafruit DHT](https://pypi.org/project/Adafruit-DHT/)
-   Node.js v11
    -   Node v11 was the last Node version supported on armv6l devices.
-   `npm`
    -   Will be packaged with Node.

### Raspberry Pi Setup

This explains how to initialize a Raspberry Pi to run the code in this repository.

If you only want to run the code on your local machine you can skip this section.

1. Write the Raspberry OS 32-Bit (Debian/Bullseye) image to an SD card using [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
    - Enable SSH, keep the username as "pi", and assign a password in the settings before writing the OS.
    - Click [here](https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2022-09-26/2022-09-22-raspios-bullseye-armhf-full.img.xz) to download the image manually.
2. Insert the SD card into the Raspberry Pi and log into it via SSH using the username and password defined in step 1.
3. Navigate into the **install/** directory and run `sh install`. This will install all dependencies in **embedded/**, **frontend/**, and **backend/**, install the `systemd` service files, start the services, and finally enable the services.
4. Visit http://localhost:3000 to see the web application.
