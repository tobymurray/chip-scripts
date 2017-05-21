import CHIP_IO.GPIO as GPIO
import time

PIN_ZERO = "XIO-P0"
PIN_ONE = "XIO-P1"

print("Setting the default state")

GPIO.setup(PIN_ZERO, GPIO.OUT)
GPIO.output(PIN_ZERO, GPIO.HIGH)

GPIO.setup(PIN_ONE, GPIO.OUT)
GPIO.output(PIN_ONE, GPIO.HIGH)

response = ""
forwards = True

while response != "q":
        response = input("What would you like to do? (\"on\", \"off\", \"change\", \"q\"): ")
        if response == "on":
                print("Turning the screwdriver on")
                time.sleep(0.5)
                GPIO.output(PIN_ZERO, GPIO.LOW if forwards else GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(PIN_ONE, GPIO.HIGH if forwards else GPIO.LOW)
        elif response == "off":
                print("Turning the screwdriver off")
                time.sleep(0.5)
                GPIO.output(PIN_ZERO, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(PIN_ONE, GPIO.HIGH)
        elif response == "change":
                print("Changing the screwdriver direction")
                forwards = not forwards
                time.sleep(0.5)
                GPIO.output(PIN_ZERO, GPIO.LOW if forwards else GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(PIN_ONE, GPIO.HIGH if forwards else GPIO.LOW)
        elif response == "q":
                break
        else:
                print("Sorry, don't know what to do with:", response)

        time.sleep(1)

print("As you're quitting, I'll ensure the drill is off")
GPIO.output(PIN_ZERO, GPIO.HIGH)
GPIO.output(PIN_ONE, GPIO.HIGH)

print("So long!");