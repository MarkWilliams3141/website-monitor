from gpiozero import StatusBoard
from gpiozero.tools import negated
from signal import pause
import ConfigParser
import io
import os.path
import pingdomlib
import time
configfile = '/config/config.ini'

HERE = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(HERE, './config/config.ini')

# Load the configuration file
with open(CONFIG_PATH) as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

# Print start up message
print('Website Monitor started using API key:' + config.get('api', 'apikey'))

# Status Board led test
sb = StatusBoard()

# Setup pingdom API
username = config.get('api', 'username')
password = config.get('api', 'password')
apikey = config.get('api', 'apikey')
api = pingdomlib.Pingdom(username, password, apikey)

# Load settings
checkinterval = config.getfloat('settings', 'checkinterval')


while True:
    # See pingdomlib.pingdom documentation to see available calls and settings
    pingdomchecks = api.getChecks()

    sitedown = False

    for check in pingdomchecks:

        # Slot 1: Marketing Site (3170812)
        # Slot 2: MC Live (3779116)
        # Slot 3: rpharms.com (4831918)
        # Slot 4: SAMS Sigma (4569933)
        # Slot 5: Unused

        if check.id == 3170812:
            if check.status == 'up':
                sb.one.lights.green.on()
                sb.one.lights.red.off()
            else:
                sitedown = True
                sb.one.lights.red.on()
                sb.one.lights.green.off()

        if check.id == 3779116:
            if check.status == 'up':
                sb.two.lights.green.on()
                sb.two.lights.red.off()
            else:
                sitedown = True
                sb.two.lights.red.on()
                sb.two.lights.green.off()

        if check.id == 4831918:
            if check.status == 'up':
                sb.three.lights.green.on()
                sb.three.lights.red.off()
            else:
                sitedown = True
                sb.three.lights.red.on()
                sb.three.lights.green.off()

        if check.id == 4569933:
            if check.status == 'up':
                sb.four.lights.green.on()
                sb.four.lights.red.off()
            else:
                sitedown = True
                sb.four.lights.red.on()
                sb.four.lights.green.off()

        if sitedown:
            sb.five.lights.red.blink()
        else:
            sb.five.lights.red.off()

    time.sleep(checkinterval)
