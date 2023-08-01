import serial
import time
import datetime

microsteps = 16
day = 0

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
print("Initializing connection....")
time.sleep(3)
ser.reset_input_buffer()
print("HELLO!")
print("connected to: " + ser.portstr)
print("moving")


def get_second_hand_angle():
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    hour = now.hour
    currentsec = (hour * 3600) + (minute * 60) + second
    return (currentsec / 86400.0) * 360.0



while True:

    time.sleep(5)
    stepangle = int(get_second_hand_angle()  /360.0 * 800.0 * microsteps)
    print(stepangle)
    ser.write(('UTC_MOVE ' + str(stepangle) + '\n').encode())
    

           
#ser.close()