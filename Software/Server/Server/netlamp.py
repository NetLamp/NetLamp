from flask import Flask
app = Flask(__name__)

#import RPi.GPIO as GPIO

#PIN = 13

HELLIGKEIT = 50

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
    return str(HELLIGKEIT)

@app.route("/api/-/<int:w>")
def minus(w):
    global HELLIGKEIT
    HELLIGKEIT -= w
    if HELLIGKEIT < 0:
        HELLIGKEIT = 0
    p.ChangeDutyCycle(HELLIGKEIT)
    return str(HELLIGKEIT)
    
@app.route("/api/=/<int:w>")
def make(w):
    global HELLIGKEIT
    if 0 <= w <= 100:
        HELLIGKEIT = w
    p.ChangeDutyCycle(HELLIGKEIT)
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
    
