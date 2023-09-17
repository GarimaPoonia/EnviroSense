import Adafruit_DHT

# Set the sensor type (DHT22 or DHT11)
sensor = Adafruit_DHT.DHT22

# Set the GPIO pin where the sensor is connected
pin = 4

try:
    # Try to read data from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature:.2f}°C')
        print(f'Humidity: {humidity:.2f}%')
    else:
        print('Failed to retrieve data from the sensor')
except KeyboardInterrupt:
    print('Measurement stopped by the user')
