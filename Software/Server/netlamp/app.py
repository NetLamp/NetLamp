#!/usr/bin/python
# ~*~ Encoding: UTF-8 ~*~

from flask import Flask
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Libs"))

#import RPi.GPIO as GPIO

#PIN = 13

HELLIGKEIT = 50

try:
    HELLIGKEIT = int(open("helligkeit.txt").read())
except:
    open("helligkeit.txt", "w").write(str(HELLIGKEIT))

app = Flask(__name__.split('.')[0])

@app.route("/")
def hello():
    return open("index2.html").read()

@app.route("/api/+/<int:w>")
def plus(w):
    global HELLIGKEIT
    HELLIGKEIT += w
    if HELLIGKEIT > 100:
        HELLIGKEIT = 100
    p.ChangeDutyCycle(HELLIGKEIT)
    open("helligkeit.txt", "w").write(str(HELLIGKEIT))
    return str(HELLIGKEIT)

@app.route("/api/-/<int:w>")
def minus(w):
    global HELLIGKEIT
    HELLIGKEIT -= w
    if HELLIGKEIT < 0:
        HELLIGKEIT = 0
    p.ChangeDutyCycle(HELLIGKEIT)
    open("helligkeit.txt", "w").write(str(HELLIGKEIT))
    return str(HELLIGKEIT)
    
@app.route("/api/=/<int:w>")
def make(w):
    global HELLIGKEIT
    if 0 <= w <= 100:
        HELLIGKEIT = w
    p.ChangeDutyCycle(HELLIGKEIT)
    open("helligkeit.txt", "w").write(str(HELLIGKEIT))
    return str(HELLIGKEIT)

#@app.route("/2")
#def i2():
#    return open("index2.html").read()

import pwmInterface.Arduino as Arduino
p = Arduino.PWM("/dev/ttyACM0")

if __name__ == "__main__":
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(PIN, GPIO.OUT)
    
    #p = GPIO.PWM(PIN, 50)
    #p.start(HELLIGKEIT)
    app.run(host='')
    
