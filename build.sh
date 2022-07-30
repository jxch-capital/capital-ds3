#!/bin/bash
sudo docker buildx build --platform=linux/amd64  -t  jxch/capital-ds3:$(date +%Y%m%d) -t jxch/capital-ds3:latest . --push