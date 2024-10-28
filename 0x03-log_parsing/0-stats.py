#!/usr/bin/python3
import sys

# Initialize variables
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0

# Function to print metrics
def print_metrics(total_size, status_codes):
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Main loop to process each line from stdin
line_count = 0
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        code = parts[-2]
        size = parts[-1]

        # Accumulate metrics
        if code in status_codes:
            status_codes[code] += 1
        total_size += int(size)
        line_count += 1

        # Print every 10 lines
        if line_count % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    # Final print on interruption
    print_metrics(total_size, status_codes)
    raise

