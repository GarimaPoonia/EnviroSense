#An additional field location is added to the data entry to store the location where the data was collected.

import json
import os

class EnvironmentalDataStorage:
    def __init__(self, data_folder):
        self.data_folder = data_folder

        # Create the data folder if it doesn't exist
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

    def create_data_entry(self, timestamp, temperature, humidity, pressure, location):
        # Create a dictionary to store the environmental data
        data_entry = {
            "timestamp": timestamp,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "location": location  # Include a location field
        }

        # Convert the data entry to JSON format
        data_entry_json = json.dumps(data_entry)

        # Define a file path based on the timestamp
        file_path = os.path.join(self.data_folder, f"{timestamp}.json")

        # Write the data entry to a JSON file
        with open(file_path, "w") as file:
            file.write(data_entry_json)

    def retrieve_data(self, timestamp):
        # Define the file path based on the timestamp
        file_path = os.path.join(self.data_folder, f"{timestamp}.json")

        if os.path.exists(file_path):
            # Read the data entry from the JSON file
            with open(file_path, "r") as file:
                data_entry_json = file.read()
                data_entry = json.loads(data_entry_json)
                return data_entry
        else:
            return None

if __name__ == "__main__":
    # Define the folder where data will be stored
    data_folder = "data"

    # Initialize the EnvironmentalDataStorage object
    data_storage = EnvironmentalDataStorage(data_folder)

    # Example data entry with location information
    timestamp = "2023-09-19T12:00:00"
    temperature = 25.0
    humidity = 50.0
    pressure = 1013.25
    location = "Office"

    # Create a data entry with location
    data_storage.create_data_entry(timestamp, temperature, humidity, pressure, location)

    # Retrieve data by timestamp
    retrieved_data = data_storage.retrieve_data(timestamp)

    if retrieved_data:
        print("Retrieved Data:")
        print(retrieved_data)
    else:
        print("Data not found for the specified timestamp.")
