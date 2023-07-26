#!/usr/bin/python3
""" UTF-8 encoding"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    def is_valid_start_byte(byte):
        return (byte >> 7) == 0 or \
               (byte >> 5) == 0b110 or \
               (byte >> 4) == 0b1110 or \
               (byte >> 3) == 0b11110

    def is_valid_follow_byte(byte):
        return (byte >> 6) == 0b10

    follow_bytes_expected = 0

    for num in data:
        num = num & 0xFF

        if follow_bytes_expected == 0:
            if not is_valid_start_byte(num):
                return False

            if num >> 7 == 0:
                follow_bytes_expected = 0
            elif num >> 5 == 0b110:
                follow_bytes_expected = 1
            elif num >> 4 == 0b1110:
                follow_bytes_expected = 2
            elif num >> 3 == 0b11110:
                follow_bytes_expected = 3
            else:
                return False
        else:
            if not is_valid_follow_byte(num):
                return False

            follow_bytes_expected -= 1

    return follow_bytes_expected == 0
