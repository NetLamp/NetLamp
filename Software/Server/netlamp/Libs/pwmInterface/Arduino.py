import serial

class PWM(object):
    CALLIBRATION = 255

    def __init__(self, port="/dev/ttyACM0"):
        self.port = port

    def start(self, duty):
        with serial.Serial(self.port) as con:
            con.write(chr(int(self.CALLIBRATION*(duty/100.))))

    def ChangeDutyCycle(self, duty):
        self.start(duty)

    def stop(self):
        self.con.close()
