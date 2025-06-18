#!/usr/bin/python

import sys
import logging

# print("PYTHONPATH:", sys.path, file=sys.stderr)

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/joan/src/flask-mib-browser")
 
from app import app as application
application.secret_key = 'fhkjdskjgf'
