#!/usr/bin/env python3
import os
import subprocess
import datetime

# Configure backup parameters
SOURCE_DIRECTORY = '/path/to/source'
DESTINATION_DIRECTORY = '/path/to/destination'
BACKUP_REPORT = 'backup_report.log'

# Perform backup using rsync
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_command = f"rsync -avz {SOURCE_DIRECTORY} {DESTINATION_DIRECTORY}/backup_{current_time}"

# Execute the backup command
result = subprocess.run(backup_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Write the report to a log file
with open(BACKUP_REPORT, 'a') as report_file:
    report_file.write(f"Backup performed at {current_time}\n")
    report_file.write(f"Command: {backup_command}\n")
    report_file.write(f"Return code: {result.returncode}\n")
    report_file.write(f"Output: {result.stdout.decode()}\n")
    report_file.write(f"Error: {result.stderr.decode()}\n")
    report_file.write(f"{'-'*60}\n")

# Check if the backup was successful
if result.returncode != 0:
    print("Backup failed. Check the backup report for details.")
else:
    print("Backup completed successfully.")

