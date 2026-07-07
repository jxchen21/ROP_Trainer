#!/bin/bash

IMAGE="rop_trainer"
PLATFORM="linux/amd64"

if ! docker image inspect "$IMAGE" &>/dev/null; then
    echo "[*] Image not found, building..."
    docker build --platform "$PLATFORM" -t "$IMAGE" .
else
    echo "[*] Image already exists, skipping build..."
fi

docker run --rm \
           --platform "$PLATFORM" \
           --security-opt seccomp=unconfined \
           -v "${PWD}:/ROP_Trainer" \
           -it "$IMAGE" bash