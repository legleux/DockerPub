#!/bin/env bash

IFS=':' read -r -a array <<< "$1"

IMAGE="${array[0]}"
TAG="${array[1]}"

cmdd="docker image pull $IMAGE:$TAG"
result=$($cmdd > /dev/null 2>&1)
exit $result
