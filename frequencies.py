"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        string_item = str(item)
        count = 1 + frequencies.get(string_item, 0)
        frequencies[string_item] = count

    return frequencies
