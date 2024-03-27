#!/usr/bin/python3

import sys
from collections import defaultdict

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        print("{}: {}".format(code, count))

def parse_line(line):
    parts = line.split()
    if len(parts) != 10 or parts[8] != '"GET' or parts[9] != '/projects/260':
        return None
    try:
        status_code = int(parts[7])
        file_size = int(parts[8])
        return (status_code, file_size)
    except (ValueError, IndexError):
        return None

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

