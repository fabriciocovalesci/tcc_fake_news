#!/bin/bash

# build image
docker build -t acta_bot . 

# change tag recent
docker tag acta_bot:latest fabriciocov/acta_bot:latest

# Push to repository - docker hub
docker push fabriciocov/acta_bot:latest