#!/usr/bin/python3

""" Script that reads stdin line by line and computes metrics """

import sys


def print_statistics(status_codes, total_size):
    """ Prints information """
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_codes.items()):
        if count != 0:
            print(f"{status_code}: {count}")


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                "404": 0, "405": 0, "500": 0}

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_statistics(status_codes, total_size)

        line_parts = line.split()
        count += 1

        try:
            total_size += int(line_parts[-1])
        except ValueError:
            pass

        try:
            status_code = line_parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            pass

    print_statistics(status_codes, total_size)

except KeyboardInterrupt:
    print_statistics(status_codes, total_size)
    raise
