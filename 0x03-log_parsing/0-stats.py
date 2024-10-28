#!/usr/bin/python3
import sys

# Initialize variables to keep track of total file size and status codes count
total_size = 0
status_codes_count = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}

def print_stats():
    """Prints the metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate line format
        if len(parts) < 9:
            continue

        # Parse the file size
        try:
            file_size = int(parts[-1])
            total_size += file_size
        except ValueError:
            continue

        # Parse the status code
        status_code = parts[-2]
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics if interrupted by keyboard (CTRL + C)
    print_stats()
    raise

# Print final statistics at the end of input
print_stats()

