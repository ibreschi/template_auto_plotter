## Install Docker on mac
https://apple.stackexchange.com/questions/373888/how-do-i-start-the-docker-daemon-on-macos

## build docker image
docker build --tag test_graph .

## run container with port
docker run -p 8080:9090 test_graph:latest

## List runnin containers
docker ps
## Go inside the docker container
docker exec -it 75c1e53c0044  bash

## Test if server replies
curl localhost:8080

## On macos
docker-machine ip default
curl 192.168.99.100:8080
