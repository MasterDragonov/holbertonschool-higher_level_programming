#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file.

    If the output file already exists, it is completely replaced.

    Args:
        data (dict): A Python dictionary containing data to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file to recreate a Python dict.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
