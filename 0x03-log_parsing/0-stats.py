#!/usr/bin/python3
import sys

# Initialize variables to store file size and status codes
total_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

def print_stats():
    """Prints accumulated metrics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Check if line contains at least 7 parts (minimum valid format)
        if len(parts) < 7:
            continue
        
        # Extract file size and status code
        file_size = parts[-1]
        status_code = parts[-2]
        
        # Update total file size
        try:
            total_file_size += int(file_size)
        except ValueError:
            continue  # Skip if file_size is not an integer
        
        # Update status code count if valid
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print final statistics
print_stats()

