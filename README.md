# RaspberryPi Website Monitor

A Python script to poll the Pingdom API and display real-time uptime report on RaspberryPi LED status board.


### Quick Start

Assuming RaspberryPi with python environment.

1. Create config.ini in the /config directory.
2. username, password, and apikey must be included in the config file. See config.ini.example for example.
3. Run script with `python main.py` or to run on startup edit `/etc/rc.local` 

The script can be also executed by creating a script such as:

`#!/bin/sh

dir="$(dirname "${0}")"
cd "${dir}"
while /bin/true; do
    python main.py
    sleep 60
done
`

Note: Edit the id codes in `main.py` to setup uptime reports. These codes can be found in the pingdom web admin.

### SSH 
The Raspberry Pi is running on the office network. It can be accessed using `ssh pi@10.11.3.194` with password `raspberry`.

### Statusboard GPIO attachment

https://github.com/ThePiHut/statusboard

https://thepihut.com/products/status-board-pro

### Installing python dependencies

Pip can be used to install the required libraries. PingdomLib and PiHut statusboard libraries are used.

statusboard: https://github.com/ThePiHut/statusboard

PingdomLib: https://pypi.org/project/PingdomLib/


