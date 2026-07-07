FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    gcc \
    gdb \
    python3 \
    python3-pip \
    file \
    checksec \
    && pip3 install ROPgadget \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash wf-user

WORKDIR /ROP_Trainer