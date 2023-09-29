#!/bin/bash
# This scrip is used to get all the http methods of a server
curl -s -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
