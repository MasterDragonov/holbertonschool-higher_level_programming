#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""
import pickle


class CustomObject:
    """A custom class representing an individual with basic attributes."""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes the CustomObject instance attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes in a structured format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current object instance and saves it to a binary file.

        Args:
            filename (str): The destination file path.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and deserializes an instance of CustomObject from a binary file.

        Args:
            filename (str): The source file path.

        Returns:
            CustomObject or None: The deserialized instance, or None if an
                                  exception occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError, AttributeError):
            return None
