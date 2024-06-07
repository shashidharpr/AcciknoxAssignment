#!/usr/bin/env python3
import re
from collections import Counter

# Path to the web server log file
LOG_FILE_PATH = '/path/to/webserver.log'

# Regular expressions for log file patterns
status_404_pattern = re.compile(r'HTTP/\d\.\d" 404 ')
most_requested_pattern = re.compile(r'GET (.+?) HTTP/\d\.\d"')

# Analyze the log file
with open(LOG_FILE_PATH, 'r') as log_file:
    log_data = log_file.read()

    # Find 404 errors
    errors_404 = status_404_pattern.findall(log_data)
    print(f"Number of 404 errors: {len(errors_404)}")

    # Find the most requested pages
    requested_pages = most_requested_pattern.findall(log_data)
    page_counts = Counter(requested_pages)
    most_common_pages = page_counts.most_common(5)
    print("Most requested pages:")
    for page, count in most_common_pages:
        print(f"{page}: {count} times")

    # Find IP addresses with the most requests (optional)
    # ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
    # ip_addresses = [ip_pattern.match(line).group(1) for line in log_data.splitlines() if ip_pattern.match(line)]
    # ip_counts = Counter(ip_addresses)
    # most_common_ips = ip_counts.most_common(5)
    # print("IP addresses with the most requests:")
    # for ip, count in most_common_ips:
    #     print(f"{ip}: {count} times

