#!/usr/bin/env python3
"""Module to convert data from CSV format to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads a CSV file and converts its data into a JSON file named data.json.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Read the data from the CSV file
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Serialize the list of dictionaries to data.json
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
