#!/bin/bash
gcc -g -static -U_FORTIFY_SOURCE -Wno-implicit-function-declaration -fno-stack-protector -no-pie -O0 -z noexecstack read_input.c ropvuln.c -o ropvuln
python3 payload.py > payload.bin
