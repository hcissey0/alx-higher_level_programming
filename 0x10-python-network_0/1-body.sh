#!/bin/bash
# This script uses GET to chek the body of a page that returns 200
curl -s -o /dev/null -w "%{http_code}%" "$1" | grep -q "200" && curl -s "$1"
