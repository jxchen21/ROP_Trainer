# ROP_Trainer

(Hopefully) simple ROP chaining demonstration, created by Johnny Chen.

# SETUP

Make sure Docker is installed! Navigate to the directory for the challenge you want to complete. To set up the image run setup.sh. To compile, run build.sh, and use the output payload.bin as an output for ropvuln (For challenge 2, this will be ropvuln_suid).

[ROPgadget Docs](https://github.com/JonathanSalwan/ROPgadget)

# CHALLENGE 0: ret2win

Simple challenge to familiarize yourself with GDB. Can you return to win() even though it's not called anywhere in the code?

[Intro to ROP](https://en.wikipedia.org/wiki/Return-oriented_programming)
[GDB Docs](https://visualgdb.com/gdbreference/commands/)
(Useful commands: disassemble, breakpoint, x command)

# CHALLENGE 1: ADMIN PASSWORD

Bank of America just pushed this C code to their server, and it seems like we can gain access to their admin login somehow... Can you exploit the vulnerable function to authenticate as an admin user?

# CHALLENGE 2: PRIVILEGE ESCALATION

Note: Access the binary for this challenge through ropvuln_suid, which will be created inside the docker image.

(ex. ropvuln_suid my_payload.bin)

This server seems to offer a function for users to open a shell and run commands; can you figure out how to exploit the vulnerable function to gain access to a root shell?

Note 2: This exploit probably will not work from within GDB, when testing make sure to use the raw binary!

[x86 syscall documentation](https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux)
(Hint: Look into the --multibr flag!)

Enjoy! Please let me know if any issues arise.
