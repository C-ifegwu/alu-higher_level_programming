#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):  # If n is out of range, return the original string
        return str
    return str[:n] + str[n+1:]  # Create a new string without the character at index n
