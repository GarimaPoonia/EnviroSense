import RPi.GPIO as GPIO
import time

# Set GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
TRIG_PIN = 11
ECHO_PIN = 12

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        # Trigger the ultrasonic sensor
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)

        # Measure the time it takes for the echo to return
        while GPIO.input(ECHO_PIN) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pulse_end = time.time()

        # Calculate distance using the speed of sound
        pulse_duration = pulse_end - pulse_start
        distance = (pulse_duration * 34300) / 2

        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)  # Check distance every 1 second
except KeyboardInterrupt:
    GPIO.cleanup()
