#!/bin/bash
# fetching response Size in byte
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
