#!/usr/bin/python3
"""Module containing a script that reads stdin and computes metrics."""
import sys

# Initialize status code counters and total bytes
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
total_bytes = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) > 4:
            status_code = parts[-2]
            try:
                byte_size = int(parts[-1])
            except ValueError:
                continue  # Skip lines where the size is not a valid integer

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            total_bytes += byte_size
            line_count += 1

        if line_count == 10:
            line_count = 0
            print(f"File size: {total_bytes}")

            for code, count in sorted(status_code_counts.items()):
                if count != 0:
                    print(f"{code}: {count}")

except Exception:
    pass

finally:
    print(f"File size: {total_bytes}")

    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print(f"{code}: {count}")
