from wsgiref.handlers import CGIHandler
from netlamp import app, p, INIT

INIT()

try:
    CGIHandler().run(app)
except:
    p.stop()
