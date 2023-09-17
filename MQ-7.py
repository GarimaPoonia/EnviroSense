import RPi.GPIO as GPIO
import time

# Set GPIO mode and pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

try:
    while True:
        # Read the digital output from the MQ-7 sensor
        if GPIO.input(7) == GPIO.HIGH:
            print("Gas detected!")
        else:
            print("No gas detected.")
        time.sleep(1)  # Check every 1 second
except KeyboardInterrupt:
    GPIO.cleanup()
