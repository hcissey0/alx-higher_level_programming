#!/bin/bash
# This script is used to do catch me if you can
curl -s -X PUT "You got me!" -w "%{stdout}" "0.0.0.0:5000/catch_me"
