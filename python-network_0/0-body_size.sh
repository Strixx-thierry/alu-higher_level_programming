#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
size=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo "$size"
