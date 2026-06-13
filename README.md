# ROP_Trainer

(Hopefully) simple ROP chaining demonstration, created by Johnny Chen.

# SETUP

Make sure Docker is installed! To set up the image run setup.sh. To compile, run build.sh, and use the output payload.bin as an output for ropvuln_suid.

[ROPgadget Docs](https://github.com/JonathanSalwan/ROPgadget)
Hint: Look into the --multibr flag!

# CHALLENGE 2: PRIVILEGE ESCALATION

Note: Access the binary for this challenge through ropvuln_suid, which will be created inside the docker image.

(ex. ropvuln_suid my_payload.bin)

This server seems to offer a function for users to open a shell and run commands; can you figure out how to exploit the vulnerable function to gain access to a root shell?

[x86 syscall documentation](https://en.wikibooks.org/wiki/X86_Assembly/Interfacing_with_Linux)

