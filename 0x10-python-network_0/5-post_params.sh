#!/bin/bash
#this requires you to POST to the passed URL using curl, and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
