#!/usr/bin/env python3
import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Check CPU usage
cpu_usage = psutil.cpu_percent()
if cpu_usage > CPU_THRESHOLD:
    logging.warning(f"High CPU usage detected: {cpu_usage}%")

# Check memory usage
memory_usage = psutil.virtual_memory().percent
if memory_usage > MEMORY_THRESHOLD:
    logging.warning(f"High memory usage detected: {memory_usage}%")

# Check disk space
disk_usage = psutil.disk_usage('/').percent
if disk_usage > DISK_THRESHOLD:
    logging.warning(f"High disk usage detected: {disk_usage}%")

# Check running processes (optional)
# for proc in psutil.process_iter(['pid', 'name']):
#     print(proc.info)

