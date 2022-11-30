#! /usr/bin/python3
import sys
import logging
logging.basicConfig(stream = sys.stderr)
sys.path.insert(0, "/var/www/reazdonor/")

from reazdonor import create_app
application = create_app()
#application.secret_key = 'team6'
