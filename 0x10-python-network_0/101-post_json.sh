#!/bin/bash
# This script is used to send post request with a json
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
