#!/usr/bin/env python3
"""Module for serializing and deserializing dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary containing key-value data.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Reads an XML file and deserializes it back into a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: A reconstructed Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from the child elements
        return {child.tag: child.text for child in root}
    except Exception:
        return {}
