#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    bytes_left = 0

    for num in data:
        if bytes_left == 0:
            if (num >> 5) == 0b110:
                bytes_left = 1
            elif (num >> 4) == 0b1110:
                bytes_left = 2
            elif (num >> 3) == 0b11110:
                bytes_left = 3
            elif (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_left -= 1

    return bytes_left == 0

if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

