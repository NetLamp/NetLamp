#!/usr/bin/python
# ~*~ Encoding: UTF-8 ~*~

import sys
import os

### ggf. an den eigenen Server anpassen
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "Server"))
### Außerdem: http://flask.pocoo.org/docs/0.10/deploying/cgi/#server-setup

from wsgiref.handlers import CGIHandler
from netlamp.app import app

try:
    CGIHandler().run(app)
except:
    p.stop()
