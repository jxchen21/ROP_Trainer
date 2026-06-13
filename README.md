# ROP_Trainer

(Hopefully) simple ROP chaining demonstration, created by Johnny Chen.

# SETUP

Make sure Docker is installed! To set up the image run setup.sh. To compile, run build.sh, and use the output payload.bin as an output for ropvuln.

[ROPgadget Docs](https://github.com/JonathanSalwan/ROPgadget)

# CHALLENGE 0: ret2win

Simple challenge to familiarize yourself with GDB. Can you return to win() even though it's not called anywhere in the code?

[Intro to ROP](https://en.wikipedia.org/wiki/Return-oriented_programming)
[GDB Docs](https://visualgdb.com/gdbreference/commands/)
(Useful commands: disassemble, breakpoint, x command)

Enjoy! Please let me know if any issues arise.
