#!/bin/bash
# Script that sends a DELETE request to the URL passed as the first argument and display response
curl -sX DELETE "$1"
