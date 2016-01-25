from wsgiref.handlers import CGIHandler
from netlamp import app

try:
    CGIHandler().run(app)
except:
    p.stop()
