#!/bin/bash

echo "Initializing combined cloud compute pipeline from repository environment..."

# 1. Fire up the folder tracking monitor script in the background
./monitor_and_push.sh &

# 2. Start the main pre-existing Suwayomi server utility process
# Using exec allows the Java app to cleanly assume process control inside the container
exec java -jar /Suwayomi-Server.jar \
  --server.port=10000 \
  --suwayomi.extensions.repositories="[\"https://githubusercontent.com\"]"
