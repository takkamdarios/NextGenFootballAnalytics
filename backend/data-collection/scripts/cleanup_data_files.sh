#!/bin/bash
# scripts/cleanup_data_files.sh

# Directory where data files are stored
data_dir="/path/to/your/data/files"

# Find and remove files older than 30 days
find $data_dir -type f -mtime +30 -name '*.json' -exec rm {} +

echo "Old data files cleaned up."
