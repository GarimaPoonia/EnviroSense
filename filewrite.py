import json
import os
import time
from datetime import datetime

class EnvironmentalDataWriter:
    def __init__(self, data_folder):
        self.data_folder = data_folder

        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

    def write_data_to_file(self, temperature, humidity, pressure, location):
        # Get the current timestamp
        timestamp = datetime.now().isoformat()

        # Create a dictionary to store the environmental data
        data_entry = {
            "timestamp": timestamp,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "location": location
        }

        # Convert the data entry to JSON format
        data_entry_json = json.dumps(data_entry)

        # Define a file path based on the timestamp
        file_path = os.path.join(self.data_folder, f"{timestamp}.json")

        # Write the data entry to a JSON file
        with open(file_path, "w") as file:
            file.write(data_entry_json)

# Example usage:
if __name__ == "__main__":
    # Define the folder where data will be stored
    data_folder = "data"

    # Initialize the EnvironmentalDataWriter object
    data_writer = EnvironmentalDataWriter(data_folder)

    # Simulate data collection
    while True:
        # Replace these values with actual sensor readings
        temperature = 25.0
        humidity = 50.0
        pressure = 1013.25
        location = "Office"

        # Write data to a file
        data_writer.write_data_to_file(temperature, humidity, pressure, location)

        # Sleep for a specified interval (e.g., 1 hour)
        time.sleep(3600)  # Sleep for 1 hour before collecting data again
