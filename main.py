from gpiozero import StatusBoard
from gpiozero.tools import negated
from signal import pause
import ConfigParser
import io
import os.path
configfile = '/config/config.ini'

HERE = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(HERE, './config/config.ini')

# Load the configuration file
with open(CONFIG_PATH) as f:
    sample_config = f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))

# Get the secret API key
print('Website Monitor started using API key:' + config.get('api', 'api_key'))

# Status Board led test
sb = StatusBoard()

for strip in sb:
    strip.lights.green.source = strip.button.values
    strip.lights.red.source = negated(strip.button.values)
pause()
